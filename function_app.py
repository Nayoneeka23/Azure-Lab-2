import azure.functions as func
import azure.durable_functions as df

app = df.DFApp()


@app.orchestration_trigger(context_name="context")
def MasterOrchestrator(context: df.DurableOrchestrationContext):

    lines = yield context.call_activity("GetInputDataFn")

    map_results = []
    for line in lines:
        result = yield context.call_activity("MapperFn", line)
        map_results.extend(result)

    shuffled = yield context.call_activity("ShufflerFn", map_results)

    reduce_results = []
    for word, values in shuffled.items():
        result = yield context.call_activity("ReducerFn", (word, values))
        reduce_results.append(result)

    return reduce_results


@app.activity_trigger(input_name="dummy")
def GetInputDataFn(dummy):
    return [
        (0, "hello world"),
        (1, "hello azure durable functions"),
        (2, "hello map reduce")
    ]


@app.activity_trigger(input_name="line")
def MapperFn(line):
    line_no, text = line
    words = text.lower().split()
    return [(word, 1) for word in words]


@app.activity_trigger(input_name="pairs")
def ShufflerFn(pairs):
    shuffled = {}
    for word, count in pairs:
        if word not in shuffled:
            shuffled[word] = []
        shuffled[word].append(count)
    return shuffled


@app.activity_trigger(input_name="item")
def ReducerFn(item):
    word, values = item
    return (word, sum(values))


@app.route(route="start-mapreduce")
@app.durable_client_input(client_name="client")
async def http_start(req: func.HttpRequest, client):
    instance_id = await client.start_new("MasterOrchestrator")
    return client.create_check_status_response(req, instance_id)

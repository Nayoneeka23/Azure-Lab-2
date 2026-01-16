from locust import HttpUser, task, between


class NumericalUser(HttpUser):
    wait_time = between(0.1, 0.5)

    # Function App host (no /api, no params)
    host = "https://nayoneeka-numint-fn-ecehh3emfegecnds.switzerlandnorth-01.azurewebsites.net"

    @task
    def call_function(self):
        self.client.get(
            "/api/numerical_integral_fn",
            params={
                "code": "<your-function-key>",   # from Get Function URL
                "lower": 0.0,
                "upper": 3.14159,
                "N": 1000                      # big enough to keep CPU busy
            }
        )

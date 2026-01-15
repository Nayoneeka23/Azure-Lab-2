from locust import HttpUser, task, between


class IntegrationUser(HttpUser):
    wait_time = between(1, 3)  # Wait 1-3s between tasks

    @task
    def compute_integral(self):
        # Heavy N for load
        self.client.get("/numerical_integral/0/3.14159/100000")

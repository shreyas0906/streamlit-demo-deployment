from locust import HttpUser, task, between 


class AppUser(HttpUser):
    WAIT_TIME = between(2, 5)

    @task
    def home_page(self):
        self.client.get("/")



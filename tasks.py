import subprocess
import os

def run(cmd):
    print(f"\n🔧 Running: {cmd}\n")
    subprocess.run(cmd, shell=True)

def install():
    run("pip install -r requirements.txt")

def dev():
    # Local dev (non-Docker)
    run("uvicorn app.main:app --reload")

def migrate():
    run("alembic upgrade head")

def postman():
    run("curl http://localhost:8000/openapi.json -o openapi.json")
    run("openapi2postmanv2 -s openapi.json -o postman_collection.json -p")

def test():
    run("pytest -v --disable-warnings")

def docker():
    with open("VERSION") as f:
        version = f.read().strip()
    run(f"docker build -t sre-student-api:{version} .")
    run(f"docker run --env-file .env.local -p 8000:8000 sre-student-api:{version}")

# 🔽 Docker Compose-based workflows
def compose_up():
    run("docker-compose --env-file .env.local up --build")

def compose_down():
    run("docker-compose down")

def compose_test():
    run("docker-compose exec fastapi-web-server pytest -v --disable-warnings")

def compose_migrate():
    run("docker-compose exec fastapi-web-server alembic upgrade head")

# 🧭 CLI Dispatcher
if __name__ == "__main__":
    import sys
    task = sys.argv[1] if len(sys.argv) > 1 else None
    tasks = {
        "install": install,
        "dev": dev,
        "migrate": migrate,
        "postman": postman,
        "test": test,
        "docker": docker,
        "up": compose_up,
        "down": compose_down,
        "compose-test": compose_test,
        "compose-migrate": compose_migrate,
    }
    if task in tasks:
        tasks[task]()
    else:
        print(f"Available commands:\n  " + "\n  ".join(tasks))

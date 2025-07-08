import subprocess

def run(cmd):
    print(f"\n🔧 Running: {cmd}\n")
    subprocess.run(cmd, shell=True)

def dev():
    run("uvicorn app.main:app --reload")

def install():
    run("pip install -r requirements.txt")

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
    run(f"docker run --env-file .env.local -p 8000:8000 sre-student-api:{version} ")


# CLI dispatcher
if __name__ == "__main__":
    import sys
    task = sys.argv[1] if len(sys.argv) > 1 else None
    tasks = {
        "dev": dev,
        "install": install,
        "migrate": migrate,
        "postman": postman,
        "test": test,
        "docker": docker,
    }
    if task in tasks:
        tasks[task]()
    else:
        print(f"Available commands: {', '.join(tasks)}")

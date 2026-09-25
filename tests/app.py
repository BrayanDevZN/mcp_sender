
def test_app() -> None:

    url =  "http://localhost:8000/sender"

    import requests

    body = {
        "email": "lsouzadiasvaz@gmail.com",
        "subject": "teste",
        "body": "teste"
    }

    response = requests.post(
        url=url,
        json=body
    )

    if response.status_code >400:

        print(f"houve um erro:\ndetail:{response.text} \nstatus code:{response.status_code}")
        return

    response = response.json()

    print(f"Ação concluida com sucesso \nid:{response["id"]}")


if __name__ == "__main__":
    test_app()

    

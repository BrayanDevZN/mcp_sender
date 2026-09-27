
if __name__ == "__main__":

    import asyncio
    import sys 
    from src.service.db.conenct import engine
    from src.database.module import make_migrate

    arg = sys.argv[1]

    if arg == "make_migrate":

        asyncio.run(make_migrate(engine=engine))

    else:

        raise ValueError(f"Not expeted {arg}")


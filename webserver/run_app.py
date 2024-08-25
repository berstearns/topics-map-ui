from create_app_instance import create_app
app = create_app()
app.run(port=8001, debug=True)

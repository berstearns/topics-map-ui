from create_app_instance import create_app
app = create_app()
app.run(host="0.0.0.0", port=80, debug=True)

from app import app
from model.user_model import user_model
obj=user_model()
@app.route("/user/getfetch")
def user_getall_controller():
    return obj.user_getall_model()  
    
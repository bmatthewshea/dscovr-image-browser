from flask import Flask, render_template, request
#from flask_bootstrap import Bootstrap

import sys, json
from urllib.request import urlopen
from datetime import date

from flask_wtf import FlaskForm

from wtforms.fields import DateField
#from wtforms.validators import InputRequired
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'SHH!'

#Bootstrap(app)

#DEBUG
if __name__ == '__main__':
    app.run(debug=True)


# static constants
dscovr_api_base = "https://epic.gsfc.nasa.gov/"
# most_recent = dscovr_api_base + "api/natural"

class DateForm(FlaskForm):
    UserDate = DateField('DatePicker', format='%Y-%m-%d', validators=[DataRequired()])

#@app.route('/')
@app.route('/', methods=['POST','GET'])
def get_date():
    form = DateForm()
    if form.validate_on_submit():
      return redirect(url_for('display', SearchDate=request.args['UserDate']))
    return render_template('index.html', form=form)

@app.route('/display')
def display():
  user_date = request.args['UserDate']
  if user_date != "":

    ymd = format_user_date(user_date)

    image_list_natural  = dscovr_load_images(user_date, 'natural')
    image_list_enhanced = dscovr_load_images(user_date, 'enhanced')

    archive_n = dscovr_api_base + "archive/{}/{}/{}/{}/png/".format('natural', ymd[0], ymd[1], ymd[2])
    archive_e = dscovr_api_base + "archive/{}/{}/{}/{}/png/".format('enhanced', ymd[0], ymd[1], ymd[2])
    return render_template("display.html", user_date=user_date, archive_n=archive_n, archive_e=archive_e, image_list_natural=image_list_natural, image_list_enhanced=image_list_enhanced)
  else:
    message = 'You submitted an empty form.'
    return HttpResponse(message)

def dscovr_load_images(user_date, image_type):
#    Year, Month, Day = map(str, user_date.split('-'))
    ymd = format_user_date(user_date)
    api = dscovr_api_base + "api/{}/date/{}-{}-{}".format(image_type, ymd[0], ymd[1], ymd[2])
    try:
        data = urlopen(api)
        jdata = json.loads(data.read())
    except:
        return HttpResponse("Problem with connection. No answer. Do not abuse the API.")
    return jdata


def format_user_date(user_date):
    Year, Month, Day = map(str, user_date.split('-'))
    return Year, Month, Day

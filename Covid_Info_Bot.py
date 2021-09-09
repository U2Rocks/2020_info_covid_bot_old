from tkinter.constants import ANCHOR, CENTER, NW
import requests
import tkinter as tk


# function that obtains country info from API
def send_request(country_code, date):
    url = "https://covid-19-data.p.rapidapi.com/report/country/code"

    querystring = {"code": country_code, "date": date}

    headers = {
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
        'x-rapidapi-key': "API KEY HERE"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)
    return response


# function that parses JSON and updates labels
def update_labels(info_response, new_date):
    re_response = info_response.json()
    new_confirmed = str(re_response[0]["provinces"][0]["confirmed"])
    new_confirmed_corrected = "Confirmed Cases: " + new_confirmed
    new_recovered = str(re_response[0]["provinces"][0]["recovered"])
    new_recovered_corrected = "Recovered Cases: " + new_recovered
    new_death = str(re_response[0]["provinces"][0]["deaths"])
    new_death_corrected = "Total Deaths: " + new_death
    new_active = str(re_response[0]["provinces"][0]["active"])
    new_active_corrected = "Active Cases: " + new_active
    confirmed_number.config(text=new_confirmed_corrected)
    recovered_number.config(text=new_recovered_corrected)
    death_number.config(text=new_death_corrected)
    active_number.config(text=new_active_corrected)
    info_date.config(text=new_date)


# function that gets time and country code
def get_covid_info():
    global current_country_code
    current_country_code = country_var.get()
    if current_country_code == stored_country_code:
        return
    start_country_code_counter(1)
    # API stopped working for any date other than 2020-04-01...
    current_date = "2020-04-01"
    switch_flag()
    request_text = send_request(current_country_code, current_date)
    update_labels(request_text, current_date)


# function that creates the country code temp storage variable
def start_country_code_counter(number):
    global stored_country_code
    if number == 0:
        stored_country_code = 'USA'
    if number == 1:
        stored_country_code = current_country_code


# function that updates main label image
def update_image(filename):
    img2 = tk.PhotoImage(file=filename)
    image_label.configure(image=img2)
    image_label.image = img2


# function that switches flags
def switch_flag():
    flag_code = country_var.get()
    if flag_code == "USA":
        country_title.config(text="United States")
        img2 = flag_file_list[0]
        update_image(img2)
    if flag_code == "ARG":
        country_title.config(text="Argentina")
        img2 = flag_file_list[1]
        update_image(img2)
    if flag_code == "BRA":
        country_title.config(text="Brazil")
        img2 = flag_file_list[2]
        update_image(img2)
    if flag_code == "CAN":
        country_title.config(text="Canada")
        img2 = flag_file_list[3]
        update_image(img2)
    if flag_code == "FRA":
        country_title.config(text="France")
        img2 = flag_file_list[4]
        update_image(img2)
    if flag_code == "IND":
        country_title.config(text="India")
        img2 = flag_file_list[5]
        update_image(img2)
    if flag_code == "JPN":
        country_title.config(text="Japan")
        img2 = flag_file_list[6]
        update_image(img2)
    if flag_code == "RUS":
        country_title.config(text="Russia")
        img2 = flag_file_list[7]
        update_image(img2)
    if flag_code == "TUR":
        country_title.config(text="Turkey")
        img2 = flag_file_list[8]
        update_image(img2)
    if flag_code == "GBR":
        country_title.config(text="Great Britain")
        img2 = flag_file_list[9]
        update_image(img2)


# create root object and config it
root = tk.Tk()
root.title("Covid Information Finder")
root.geometry("550x550")
root.minsize(550, 550)
root.maxsize(550, 550)
root.config(bg="#03bafc")

# define supported countries and country flag file list
global flag_file_list
global supported_countries
flag_file_list = ['FL_US.GIF', 'FL_ARG.GIF', 'FL_BR.GIF', 'FL_CAN.GIF',
                  'FL_FR.GIF', 'FL_IND.GIF', 'FL_JA.GIF', 'FL_RU.GIF', 'FL_TU.GIF', 'FL_UK.GIF']
supported_countries = ['USA', 'ARG', 'BRA', 'CAN',
                       'FRA', 'IND', 'JPN', 'RUS', 'TUR', 'GBR']
country_var = tk.StringVar(root)
country_var.set(supported_countries[0])

# create objects for application
global select_country
global country_title
global confirmed_number
global recovered_number
global death_number
global active_number
global info_date
global img
global change_select_button
global image_label
select_country = tk.OptionMenu(root, country_var, *supported_countries)
covid_info_frame = tk.Frame(root, bg="#427ef5")
country_title = tk.Label(
    root, text="United States", font="Helvetica 16")
confirmed_number = tk.Label(
    covid_info_frame, text="100 Confirmed Cases", font="Helvetica 12 bold")
recovered_number = tk.Label(
    covid_info_frame, text="100 Recovered Individuals", font="Helvetica 12 bold")
death_number = tk.Label(
    covid_info_frame, text="100 Total Deaths", font="Helvetica 12 bold")
active_number = tk.Label(
    covid_info_frame, text="100 Active Cases", font="Helvetica 12 bold")
info_date = tk.Label(
    covid_info_frame, text="Date: 2020-04-01", font="Helvetica 12 bold")
img = tk.PhotoImage(file=flag_file_list[0])
change_select_button = tk.Button(
    root, text="Select Country", command=get_covid_info)
image_label = tk.Label(root, image=img)

# place objects onto application
select_country.grid(row=0, column=0, padx=10, pady=10)
country_title.grid(row=0, column=1, padx=10, pady=10)
change_select_button.grid(row=0, column=2, padx=10, pady=10)
image_label.grid(row=1, column=0, padx=10, pady=10, columnspan=3)
covid_info_frame.grid(row=2, column=0, padx=10, pady=10, columnspan=3)
confirmed_number.grid(row=0, column=1, padx=10, pady=10)
recovered_number.grid(row=1, column=1, padx=10, pady=10)
death_number.grid(row=2, column=1, padx=10, pady=10)
active_number.grid(row=3, column=1, padx=10, pady=10)
info_date.grid(row=4, column=1, padx=10, pady=10)


# call functions to create key variables
start_country_code_counter(0)

# start root mainloop
root.mainloop()

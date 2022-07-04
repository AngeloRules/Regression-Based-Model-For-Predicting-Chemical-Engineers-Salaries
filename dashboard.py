import streamlit as st 
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import pickle 
import plotly.express as px

data = pd.read_csv('FinalDraft.csv')
raw = pd.read_csv('combined data.csv')

with open('model_pkl', 'rb') as file:
    rfr = pickle.load(file)
user_input = np.zeros((1,110))

with st.sidebar:
    selected = option_menu(menu_title='Main Menu',
    options=['Salary Predictor','Dashboard','Data'],icons=['currency-dollar','bar-chart-fill','123'])

def postings(item):
    fig = px.bar(data[item].value_counts().head(10).sort_values(), orientation='h',
             title=f'{item}<br>(Hover for Number of Job Postings)',color_discrete_sequence=['#ff4b4b'],text_auto='.3s')
    fig.update_layout(plot_bgcolor='rgba(0,0,0,0)',paper_bgcolor='rgba(0,0,0,0)',showlegend=False)
    fig.update_traces(textposition='outside',textfont_size=12)
    st.plotly_chart(fig)

def salaries(item):
    byItem = pd.pivot_table(data=data,index=item,values='Average Salary')
    byItem = byItem.sort_values(by='Average Salary', ascending = False).head(10)
    fig = px.bar(byItem, orientation='h',
             title=f'Average Salaries{item}<br>(Hover for Average Salary)',color_discrete_sequence=['#ff4b4b'],text_auto='.3s')
    fig.update_layout(plot_bgcolor='rgba(0,0,0,0)',paper_bgcolor='rgba(0,0,0,0)',showlegend=False)
    fig.update_traces(textposition='outside',textfont_size=12)
    st.plotly_chart(fig)

def state(item):
    byInd = pd.pivot_table(data=data,index=['States'],columns=data['Sector'],aggfunc='count').drop(['Average Employee Size','Years of Experience','Average Revenue','Type of ownership','Average Salary','Size','Bachelors','Masters','PHD','Senior','Chem Eng','Salary Estimate','Coding Skill','Revenue','Region','Company Age','Company Name'
                                                                                      ,'Microsoft Skill','Founded','Full-Time','Longitude','Latitude','Location','Hourly Wage','Industry','Job Title','Simulation Software','Job Description'],axis=1)
    byInd = byInd.loc[item].dropna().head(10).sort_values(ascending=False)
    st.dataframe(byInd)

def convert_df(df):
    return df.to_csv().encode('utf-8')

stat = {
"Alabama": "AL",
"Alaska": "AK",
"Arizona": "AZ",
"Arkansas": "AR",
"California": "CA",
"Colorado": "CO",
"Connecticut": "CT",
"Delaware": "DE",
"Florida": "FL",
"Georgia": "GA",
"Hawaii": "HI",
"Idaho": "ID",
"Illinois": "IL",
"Indiana": "IN",
"Iowa": "IA",
"Kansas": "KS",
"Kentucky": "KY",
"Louisiana": "LA",
"Maine": "ME",
"Maryland": "MD",
"Massachusetts": "MA",
"Michigan": "MI",
"Minnesota": "MN",
"Mississippi": "MS",
"Missouri": "MO",
"Montana": "MT",
"Nebraska": "NE",
"Nevada": "NV",
"New Hampshire": "NH",
"New Jersey": "NJ",
"New Mexico": "NM",
"New York": "NY",
"North Carolina": "NC",
"North Dakota": "ND",
"Ohio": "OH",
"Oklahoma": "OK",
"Oregon": "OR",
"Pennsylvania": "PA",
"Rhode Island": "RI",
"South Carolina": "SC",
"South Dakota": "SD",
"Tennessee": "TN",
"Texas": "TX",
"Utah": "UT",
"Vermont": "VT",
"Virginia": "VA",
"Washington": "WA",
"West Virginia": "WV",
"Wisconsin": "WI",
"Wyoming": "WY",
"District of Columbia": "DC",
"American Samoa": "AS",
"Guam": "GU",
"Northern Mariana Islands": "MP",
"Puerto Rico": "PR",
"United States Minor Outlying Islands": "UM",
"U.S. Virgin Islands": "VI",
}


states = {
        'Alaska': 58,
        'Alabama': 59,
        'Arkansas': 60,
        'Arizona': 61,
        'California': 62,
        'Colorado': 63,
        'Connecticut': 64,
        'District of Columbia':65,
        'Delaware': 66,
        'Florida': 67,
        'Georgia': 68,
        'Hawaii': 69,
        'Iowa': 70,
        'Idaho': 71,
        'Illinois': 72,
        'Indiana': 73,
        'Kansas': 74,
        'Kentucky': 75,
        'Louisiana': 76,
        'Massachusetts': 77,
        'Maryland': 78,
        'Maine': 79,
        'Michigan':80,
        'Minnesota': 81,
        'Missouri': 82,
        'Mississippi':83,
        'Montana':84,
        'North Carolina': 85,
        'North Dakota': 86,
        'Nebraska': 87,
        'New Hampshire': 88,
        'New Jersey': 89,
        'New Mexico': 90,
        'Nevada': 91,
        'New York': 92,
        'Ohio': 93,
        'Oklahoma': 94,
        'Oregon': 95,
        'Pennsylvania': 96,
        'Rhode Island': 97,
        'South Carolina': 99,
        'South Dakota':100,
        'Tennessee': 101,
        'Texas': 102,
        'Utah': 103,
        'Virginia': 104,
        'Vermont':105,
        'Washington': 106,
        'Wisconsin': 107,
        'West Virginia': 108,
        'Wyoming':109,
        'Remote': 98
}
industries = {'Aerospace & Defense':22,
'Agriculture':23,
'Construction, Repair & Maintenance Services':24,
'Education':25,
'Energy, Mining & Utilities':26,
'Financial Services':27,
'Government & Public Administration':28,
'Healthcare':29,
'Human Resources & Staffing':30,
'Information Technology':31,
'Insurance':32,
'Management & Consulting':33,
'Manufacturing':34,
'Nonprofit & NGO':35,
'Pharmaceutical & Biotechnology':36,
'Retail & Wholesale':37,
'Transportation & Logistics':38
}

ployees = {'1 to 50 Employees':39,
    '51 to 200 Employees':45,
    '201 to 500 Employees':42,
    '501 to 1000 Employees':44,
    '1001 to 5000 Employees':41,
    '5001 to 10000 Employees':43,
    '10000+ Employees':40
}

owners = {'College / University':12,
    'Company - Private':13,
    'Company - Public':14,
    'Contract':15,
    'Government':16,
    'Hospital':17,
    'Nonprofit Organization':18,
    'Private Practice / Firm':19,
    'Self-employed':20,
    'Subsidiary or Business Segment':21
}

venue = {'Less than $1 million (USD)':57,
    '$1 to $5 million (USD)':47,
    '$5 to $10 million (USD)':54,
    '$10 to $25 million (USD)':48,
    '$25 to $50 million (USD)':52,
    '$50 to $100 million (USD)':55,
    '$100 to $500 million (USD)':50,
    '$500 million to $1 billion (USD)':56,
    '$1 to $2 billion (USD)':46,
    '$2 to $5 billion (USD)':51,
    '$5 to $10 billion (USD)':53,
    '$10+ billion (USD)':49
    }

if selected == 'Salary Predictor':
    st.title('Salary Predictor')
    first,second = st.columns([1,2])
    loc = first.selectbox('Where would you like to work?',["Remote","Alabama","Alaska","Arizona","Arkansas","California","Colorado",
    "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
    "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
    "Massachusetts","Michigan","Minnesota","Mississippi","Montana","Missouri",
    "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
    "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
    "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah","Vermont",
    "Virginia","Washington","West Virginia","Wisconsin","Wyoming"])

    location = states[loc]
    user_input[0,location] = 1

    exp = second.number_input('Years of Experience',min_value=0,max_value=25)
    user_input[0,3] = exp
    ind = st.selectbox('Sector',['Aerospace & Defense','Agriculture',
    'Construction, Repair & Maintenance Services',
    'Education',
    'Energy, Mining & Utilities',
    'Financial Services',
    'Government & Public Administration',
    'Healthcare',
    'Human Resources & Staffing',
    'Information Technology',
    'Insurance',
    'Management & Consulting',
    'Manufacturing',
    'Nonprofit & NGO',
    'Pharmaceutical & Biotechnology',
    'Retail & Wholesale',
    'Transportation & Logistics'])

    industry = industries[ind]
    user_input[0,industry] = 1

    one, two = st.columns([2,1])
    company = one.selectbox('Company Ownership',['College / University',
    'Company - Private',
    'Company - Public',
    'Contract',
    'Government',
    'Hospital',
    'Nonprofit Organization',
    'Private Practice / Firm',
    'Self-employed',
    'Subsidiary or Business Segment'])

    own = owners[company]
    user_input[0,own] = 1

    age = two.number_input('Company Age',min_value=0,max_value=1000)
    uno,deux = st.columns([1,2])
    user_input[0,6] = age

    skill = uno.radio(horizontal=True,label='Microsoft Skill',options=['Yes','No'])
    if skill == 'Yes':
         user_input[0,8] = 1

    degrees = deux.multiselect('Academic Level',['B.Sc','M.Sc','PhD'])
    for degree in degrees:
        if 'B.Sc' in degree:
            user_input[0,0] = 1
        elif 'M.Sc' in degree:
            user_input[0,1] = 1
        elif 'PhD' in degree:
            user_input[0,2] = 1
    
    un,due,trois = st.columns([1,1,1])
    senior = un.radio(horizontal=True,options=['Yes','No'],label='Senior Role')
    if senior == 'Yes':
         user_input[0,7] = 1

    coding = due.radio(horizontal=True,options=['Yes','No'],label='Coding Skill')
    if coding == 'Yes':
         user_input[0,4] = 1

    hourly = trois.radio(horizontal=True,options=['Yes','No'],label='Hourly Pay')
    if hourly == 'Yes':
         user_input[0,5] = 1

    five,six = st.columns([2,1])
    employ = six.selectbox('Number of Employees',[
    '51 to 200 Employees',
    '201 to 500 Employees',
    '501 to 1000 Employees',
    '1001 to 5000 Employees',
    '5001 to 10000 Employees',
    '10000+ Employees',
])
    employs = ployees[employ]
    user_input[0,employs] = 1

    revenue = five.selectbox('Company Revenue',['Less than $1 million (USD)',
    '$1 to $5 million (USD)',
    '$5 to $10 million (USD)',
    '$10 to $25 million (USD)',
    '$25 to $50 million (USD)',
    '$50 to $100 million (USD)',
    '$100 to $500 million (USD)',
    '$500 million to $1 billion (USD)',
    '$1 to $2 billion (USD)',
    '$2 to $5 billion (USD)',
    '$5 to $10 billion (USD)',
    '$10+ billion (USD)'])
    money = venue[revenue]
    user_input[0,money] = 1

    role,major,soft = st.columns([1,1,1])
    full = role.radio(horizontal=True,options=['Yes','No'],label='Full-Time')
    if full == 'Yes':
         user_input[0,9] = 1

    chem = major.radio(horizontal=True,options=['Yes','No'],label='Chemical Engineering Major')
    if chem == 'Yes':
         user_input[0,10] = 1

    sim = soft.radio(horizontal=True,options=['Yes','No'],label='Simulation Software?')
    if sim == 'Yes':
         user_input[0,11] = 1
    if st.button('Predict'):
        mean = data['Average Salary'].mean()
        prediction = rfr.predict(user_input)
        
        st.success(f'Your expected Salary is ${prediction[0]}')
        agg = pd.DataFrame(data = [mean,prediction[0]],index=['Mean Salary','Predicted Salary'])
        fig = px.bar(orientation='h',data_frame=agg,title='Predicted Salary VS Mean',color_discrete_sequence=[['lightslategray','#ff4b4b']],text_auto='.3s')
        fig.update_layout(xaxis_visible=False,plot_bgcolor='rgba(0,0,0,0)',paper_bgcolor='rgba(0,0,0,0)',showlegend=False)
        fig.update_traces(textposition='inside',textfont_size=12)
        for item in fig.data:
            item['width'] = 0.3
        fig.update_layout(bargap=0)
        st.plotly_chart(fig)


elif selected == 'Dashboard':
    st.title('Salary DashBoard')
    jobs,locations,median_salary = st.columns([1,1,1])
    jobs.metric(label='Number of Jobs',value=data['Job Title'].count())
    locations.metric(label='Number of Unique Locations',value=data['Location'].nunique())
    median_salary.metric(label='Average Salary',value='$'+str(data['Average Salary'].mean()))
    st.metric(label='Average Experience',value=round(data['Years of Experience'].mean(),2))
    maps = st.selectbox(label='Choropleth',options=['Job Posting','Salary Distribution'])
    if maps == 'Job Posting':
        figure = px.scatter_mapbox(data_frame=data, lat="Latitude", lon="Longitude", hover_name="Location", hover_data=['Sector','Average Salary','Job Title','Company Name'],
                        color_discrete_sequence=["#ff4b4b"], zoom=3, height=600,title='<br>Job Posting By Location')
        figure.update_layout(mapbox_style="open-street-map")
        figure.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        st.plotly_chart(figure)
        
    elif maps == 'Salary Distribution':
        byStates = pd.pivot_table(data=data,index='States',values='Average Salary')
        byStates = byStates.reset_index()
        fig = px.choropleth(data_frame= byStates,locations='States', locationmode='USA-states', color='Average Salary',
                            color_continuous_scale="reds",
                           range_color=(0, 140000),
                           scope="usa",
                            title='<br>Salary Distribution by State'
                          )
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        st.plotly_chart(fig)
    job = st.selectbox(label='Number of Job Opportunities by',options=['Company Name','Sector','Region','States',
    'Type of ownership','Revenue'])
    postings(job)
    salary = st.selectbox(label='Average Salary by',options=['Company Name','Sector','Region','States',
    'Type of ownership','Revenue','Coding Skill','Senior','Microsoft Skill','Full-Time','Chem Eng',
    'Bachelors','Masters','PHD','Simulation Software','Hourly Wage'])
    salaries(salary)
    sect = st.selectbox(label='Type of Industry by State',options=["Alabama","Alaska","Arizona","Arkansas","California","Colorado",
    "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
    "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
    "Massachusetts","Michigan","Minnesota","Mississippi","Montana","Missouri",
    "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
    "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
    "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
    "Virginia","Washington","West Virginia","Vermont","Wisconsin","Wyoming"])
    state(stat[sect])
    


elif selected == 'Data':
    select = st.selectbox(label='View Data',options=['Cleaned Data','Raw Data'])
    if select == 'Cleaned Data':
        csv = convert_df(data)
        st.dataframe(data.drop(['Unnamed: 0'],axis=1))
        st.download_button(label='Download Data',file_name='cleaned_data.csv',data=csv)
    elif select == 'Raw Data':
        csv = convert_df(raw)
        st.dataframe(raw)
        st.download_button(label='Download Data',file_name='raw_data.csv',data=csv)

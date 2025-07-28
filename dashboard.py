import pandas as pd
import streamlit as st
import seaborn as sns


df = pd.read_csv("cleaned_student_mental_health_dataset.csv")
st.title("🧑‍🎓Student Mental Health Dashboard")
st.write("### Here you can analyse the student mental health")

age_range = st.sidebar.slider("Select Age",int(df['age'].min()),int(df['age'].max()),(18,45))
year_of_study = st.sidebar.multiselect("Select year of study",sorted(df['study_year'].unique()))
courses = st.sidebar.multiselect("Select Courss",df['course'].unique())

filtered_df = df[(df['age']>age_range[0])&(df['age']<age_range[1])&(df['study_year'].isin(year_of_study))&(df['course'].isin(courses))]

import matplotlib.pyplot as plt

st.subheader("Mental Health status")
if not filtered_df.empty:

 mental_health_counts ={
  'Depression' : filtered_df['depression'].value_counts().get('Yes',0),
  'Anxiety' : filtered_df['anxiety'].value_counts().get('Yes',0),
  'Panic Attack' : filtered_df['panic_attack'].value_counts().get('Yes',0)
 }
 fig1 , ax1=plt.subplots()
 ax1.bar(mental_health_counts.keys(),mental_health_counts.values(),color=['orange','blue','yellow'])
 st.pyplot(fig1)

 
else :
 st.warning("⚠️ No data available for the selected filters.")


st.subheader("CGPA vs Mental Health Status")

if not filtered_df.empty:
    filtered_df['status'] =(
       'depression:'+filtered_df['depression']+'|'+
       'anxiety:'+filtered_df['anxiety']+'|'+
       'panic_attack:'+filtered_df['panic_attack']
    )
    fig1 , ax1=plt.subplots()
    sns.scatterplot(data=filtered_df,x=filtered_df.index,y='cgpa',hue='status',palette='Set2')
    
    ax1.set_xlabel("Student Index")
    ax1.set_ylabel("Cgpa")
    st.pyplot(fig1)
    


else:
    st.warning("⚠️ No data available for the selected filters.")


st.subheader("Gender vs Mental Health Status")

if not filtered_df.empty:
    filtered_df['status'] =(
       'depression:'+filtered_df['depression']+'|'+
       'anxiety:'+filtered_df['anxiety']+'|'+
       'panic_attack:'+filtered_df['panic_attack']
    )
    fig1 , ax1=plt.subplots()
    sns.scatterplot(data=filtered_df,x=filtered_df.index,y='gender',hue='status',palette='Set2')
    
    ax1.set_xlabel('Student Index')
    ax1.set_ylabel('Gender')
    st.pyplot(fig1)
    


else:
    st.warning("⚠️ No data available for the selected filters.")

st.subheader("Treatment response for each mental health condition")

if not filtered_df.empty:
   col1,col2,col3 = st.columns(3)

   with col1:
      st.write("Depression")
      dep = filtered_df[filtered_df['depression']=='Yes']['treatment'].value_counts()
      if not dep.empty: 
        fig1, ax1 = plt.subplots()
        ax1.pie(dep, labels=dep.index, autopct='%1.1f%%', startangle=90, colors=['lightgreen', 'lightcoral'])
        ax1.axis('equal')
        st.pyplot(fig1)
      else:
         st.warning("No students with depression")
          

   with col2:
        st.write("**Anxiety**")
        anx_treat = filtered_df[filtered_df['anxiety'] == 'Yes']['treatment'].value_counts()
        if not anx_treat.empty:
          fig2, ax2 = plt.subplots()
          ax2.pie(anx_treat, labels=anx_treat.index, autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightcoral'])
          ax2.axis('equal')
          st.pyplot(fig2)
        else:
          st.warning("No students with anxiety")   

    
   with col3:
        st.write("**Panic Attack**")
        pan_treat = filtered_df[filtered_df['panic_attack'] == 'Yes']['treatment'].value_counts()
        if not pan_treat.empty:
          fig3, ax3 = plt.subplots()
          ax3.pie(pan_treat, labels=pan_treat.index, autopct='%1.1f%%', startangle=90, colors=['violet', 'lightcoral'])
          ax3.axis('equal')
          st.pyplot(fig3)
        else:
          st.warning("No students with panic attacks")      

else:
   st.warning("⚠️ No data available for the selected filters.")








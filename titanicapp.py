import streamlit as st
import pickle

st.title('Titanic Survival Prediction Model')

#Load the pretrained model
with open('titanicpickle.pkl', 'rb') as modelFile:
    model=pickle.load(modelFile)

#Function to make prediction
def PredictionFunction(Pclass, Sex, Age, SibSp, Parch, Fare, Embarked):
    try:
        prediction= model.predict([[Pclass, Sex, Age, SibSp, Parch, Fare, Embarked]]) #tabular data usually return a list value
        return 'Survived' if prediction[0] == 1 else 'Did not survive'
    except:
        print('Something went wrong!')

st.sidebar.markdown(
    """
1. Enter the Passenger Details in the Form.
2. Click 'Predict', to see the Survival Result.
3. Adjust Values to Test Different Scenarios.
"""
)
st.sidebar.info('Example: A 30 years old male, 3rd class, $20 fare, traveling alone from port Southempton.')

def main():
    st.subheader('Enter Passenger Details: ')
    col1, col2, = st.columns(2)
    #organize the inputs in columns
    with col1:
        Pclass= st.selectbox('Passenger Class', options= [1,2,3])
        Sex= st.radio('Gender', options=['male', 'female'])
        Age= st.slider('Age: ', min_value=0, max_value=100, value=25)

    with col2:
        SibSp= st.slider('Siblings/ Spouses Aboard: ', min_value=0, max_value=10, value=0)
        Parch= st.slider('Parents/ Children Aboard: ', min_value=0, max_value=10, value=0)
        Fare= st.slider('Fare($)', min_value=0, max_value=500, value=0)
        Embarked= st.radio('Port of Embarkation: ', options=['C', 'Q', 'S'])

    #Convert the catagorical inputs to numeric values
    if Sex== 'female':
        Sex=1
    else:
        Sex=0
    Embarked = {'C':0, 'Q':1, 'S':2}[Embarked]

    #Button to Predict
    if st.button('Predict'):
        result= PredictionFunction(Pclass, Sex, Age, SibSp, Parch, Fare, Embarked)
        st.info(result)



main()
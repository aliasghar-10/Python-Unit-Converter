import streamlit as st

def convert_length(value, from_unit, to_unit):
    conversion_factors = {
        "meter": 1,
        "kilometer": 1000,
        "mile": 1609.34,
        "yard": 0.9144,
        "feet": 0.3048,
    }
    return value * conversion_factors[from_unit] / conversion_factors[to_unit]

def convert_weight(value, from_unit, to_unit):
    conversion_factors = {
        "kilogram": 1,
        "gram": 0.001,
        "pound": 0.453592,
        "ounce": 0.0283495,
    }
    return value * conversion_factors[from_unit] / conversion_factors[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "celsius" and to_unit == "fahrenheit":
        return (value * 9/5) + 32
    if from_unit == "fahrenheit" and to_unit == "celsius":
        return (value - 32) * 5/9
    if from_unit == "celsius" and to_unit == "kelvin":
        return value + 273.15
    if from_unit == "kelvin" and to_unit == "celsius":
        return value - 273.15
    if from_unit == "fahrenheit" and to_unit == "kelvin":
        return (value - 32) * 5/9 + 273.15
    if from_unit == "kelvin" and to_unit == "fahrenheit":
        return (value - 273.15) * 9/5 + 32

def main():
    st.title("Unit Converter")

    st.sidebar.header("Choose Conversion Type")
    conversion_type = st.sidebar.selectbox(
        "Conversion Type", ["Length", "Weight", "Temperature"]
    )

    if conversion_type == "Length":
        st.subheader("Length Conversion")
        value = st.number_input("Enter the value to convert:", min_value=0.0, step=0.1)
        from_unit = st.selectbox("From Unit", ["meter", "kilometer", "mile", "yard", "foot"])
        to_unit = st.selectbox("To Unit", ["meter", "kilometer", "mile", "yard", "foot"])
        if st.button("Convert"):
            result = convert_length(value, from_unit, to_unit)
            st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

    elif conversion_type == "Weight":
        st.subheader("Weight Conversion")
        value = st.number_input("Enter the value to convert:", min_value=0.0, step=0.1)
        from_unit = st.selectbox("From Unit", ["kilogram", "gram", "pound", "ounce"])
        to_unit = st.selectbox("To Unit", ["kilogram", "gram", "pound", "ounce"])
        if st.button("Convert"):
            result = convert_weight(value, from_unit, to_unit)
            st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

    elif conversion_type == "Temperature":
        st.subheader("Temperature Conversion")
        value = st.number_input("Enter the value to convert:", step=0.1)
        from_unit = st.selectbox("From Unit", ["celsius", "fahrenheit", "kelvin"])
        to_unit = st.selectbox("To Unit", ["celsius", "fahrenheit", "kelvin"])
        if st.button("Convert"):
            result = convert_temperature(value, from_unit, to_unit)
            st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

if __name__ == "__main__":
    main()

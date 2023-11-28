// Function to validate the user's full name
export function validateFullName(fullname) {
    let error = "";
    if (fullname.trim() === "") {
        error = "Please enter your name";
    } else if (fullname.length < 3) {
        error = "Name is too short";
    }
    //An error message if the full name is invalid
    return error;
}
// Function to validate the user's phone number
export function validatePhone(phone) {
    const regexmob = /^\d{10}$/;
    let error = "";

    if (phone.trim() == "") {
        error = "Please enter your phone number";
        return error;
    } else if (!regexmob.test(phone)) {
        error = "Please enter a valid phone number";
        return error;
    }
    // An error message if the phone number is invalid
    return error;
}
// Function to validate the user's email address
export function validateEmail(email) {
    const emailpattern =
        /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
    let error = "";

    if (email.trim() == null) {
        error = "Please enter your email";
        return error;
    } else if (!emailpattern.test(email)) {
        error = "Please enter a valid email address";
        return error;
    }
    // console.log(error);
    //An error message if the email address is invalid
    return error;
}
// Function to validate the user's image URL
export function validateImageUrl(imageurl) {
    const urlpattern =
        /(?:https?):\/\/(\w+:?\w*)?(\S+)(:\d+)?(\/|\/([\w#!:.?+=&%!\-\/]))?/;
    let error = "";
    if (imageurl.trim() == "") {
        error = "Please enter image URL";
        return error;
    } else if (!urlpattern.test(imageurl)) {
        error = "Please enter a valid image URL";
        return error;
    }
    // console.log(error);
    //An error message if the image URL is invalid
    return error;
}
// Function to validate the user's summary
export function validateSummary(summary) {
    let error = "";
    if (summary.trim() == "") {
        error = "summary cannot be empty";
    } else if (summary.length < 3) {
        error = "summary is too short";
    }
    //   An error message if the summary is invalid
    return error;
}
// Function to validate the user's address
export function validateAddress(address) {
    let error = "";
    if (address.trim() == "") {
        error = "Please enter your address";
    }
    //   An error message if the address is invalid
    return error;
}
// Function to validate the user's city
export function validateCity(city) {
    let error = "";
    if (city.trim() == "") {
        error = "Please enter your city";
    }
    //   An error message if the city is invalid
    return error;
}
// Function to validate the user's state
export function validateState(state) {
    let error = "";
    if (state.trim() == "") {
        error = "Please enter your state";
    }
    //   An error message if the state is invalid
    return error;
}
// Function to validate the user's country
export function validateCountry(country) {
    let error = "";
    if (country.value == "") {
        error = "Please select your country";
    }
    //   An error message if the country is invalid
    return error;
}
// Function to validate the user's qualification
export function validateQualification(qualification) {
    let error = "";
    if (qualification.trim() == "") {
        error = "Please enter your qualification";
    }
    //   An error message if the qualification is invalid
    return error;
}
// Function to validate the user's course name
export function validateCourseName(course_name) {
    let error = "";
    if (course_name.trim() == "") {
        error = "Please enter your course name";
    }
    //   An error message if the course name is invalid
    return error;
}
// Function to validate the user's insttute
export function validateInstitute(institute) {
    let error = "";
    if (institute.trim() == "") {
        error = "Please enter your institute name";
    }
    //   An error message if the insttute is invalid
    return error;
}
// Function to validate the user's location
export function validateInstituteLocation(institute_location) {
    let error = "";
    if (institute_location.trim() == "") {
        error = "Please enter your institute location";
    }
    //   An error message if the location is invalid
    return error;
}
export function validateZipcode(zipcode) {
    let error = "";
    if (zipcode.trim() == "") {
        error = "Please enter your zipcode";
    }
    //   An error message if the zipcode is invalid
    return error;
}
export function validateStartDate(academic_start_date){
    let error = "";
    if (academic_start_date == "" || academic_start_date == null){
        error = "please enter your academic start date";
        return error;
    }
    else{
        error = "";
        return error;
    }
}
export function validateEndDate(academic_end_date){
    let error = "";
    if (academic_end_date == "" || academic_end_date == null){
        error = "please enter your academic end date";
        return error;
    }
    else{
        error = "";
        return error;
    }
}




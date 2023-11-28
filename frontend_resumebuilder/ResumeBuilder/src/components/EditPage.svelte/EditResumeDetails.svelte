<script>
  // import the components
  import Icon from "@iconify/svelte";
  import { prevent_default } from "svelte/internal";
  import PersonalDetails from "../ResumeDetails/PersonalDetails.svelte";
  import AddressDetails from "../ResumeDetails/AddressDetails.svelte";
  import EducationDetails from "../ResumeDetails/EducationDetails.svelte";
  import WorkExperienceDetails from "../ResumeDetails/WorkExperienceDetails.svelte";
  import SkillsDetails from "../ResumeDetails/SkillsDetails.svelte";
  import SocialMediaDetails from "../ResumeDetails/SocialMediaDetails.svelte";
  import LanguageDetails from "../ResumeDetails/LanguageDetails.svelte";
  import ProjectDetails from "../ResumeDetails/ProjectDetails.svelte";
  import ButtonInput from "../FormInputs/ButtonInput.svelte";

  // Import validation functions
  import {
    validateEmail,
    validatePhone,
    validateImageUrl,
    validateFullName,
    validateSummary,
    validateAddress,
    validateCity,
    validateState,
    validateCountry,
    validateQualification,
    validateCourseName,
    validateInstitute,
    validateInstituteLocation,
    validateZipcode,
  } from "../../assets/js/validation";

  let editId = window.history.state.editId;
  // console.log(editId);

  let successMessage = "";
  let warningMessage = "";
  let showMessage = "";
  let showError = false;

  export let updateForm = "";
  export let full_name = "";
  export let email = "";
  export let phone_number = "";
  export let image_url = "";
  export let summary = "";
  export let address_line = "";
  export let street_name = "";
  export let city = "";
  export let state = "";
  export let country = "";
  export let zipcode = "";
  export let educationDetails = [];
  export let workExperienceDetails = [];
  export let skillDetails = [];
  export let socialMediaDetails = [];
  export let languageDetails = [];
  export let projectDetails = [];

  // Reset the values of the form variables to their initial state
  function resetForm() {
    document.getElementById("formId").reset();
  }

  // Fetch resume data from the API using the editId
  async function apiFetchResumeById(editId) {
    if (editId != "") {
      const response = await fetch(`http://127.0.0.1:8000/resume/${editId}`, {
        method: "GET",
      });
      const data = await response.json();
      // console.log(data);
      // Extract relevant data from the API response
      full_name = data.personalDetails.full_name;
      email = data.personalDetails.email;
      phone_number = data.personalDetails.phone_number;
      image_url = data.personalDetails.image_url;
      summary = data.personalDetails.summary;
      address_line = data.addressDetails.address_line;
      street_name = data.addressDetails.street_name;
      city = data.addressDetails.city;
      state = data.addressDetails.state;
      country = data.addressDetails.country;
      zipcode = data.addressDetails.zipcode;
      educationDetails = data.educationDetails;
      workExperienceDetails = data.workExperienceDetails;
      projectDetails = data.projectDetails;
      skillDetails = data.skillDetails;
      socialMediaDetails = data.socialMediaDetails;
      languageDetails = data.languageDetails;
    }
  }
  apiFetchResumeById(editId);

  // Function to handle form submission
  async function updateDetails() {
    updateForm = {
      personalDetails: {
        full_name,
        email,
        phone_number,
        image_url,
        summary,
      },
      addressDetails: {
        address_line,
        street_name,
        city,
        state,
        country,
        zipcode,
      },
      educationDetails,
      workExperienceDetails,
      socialMediaDetails,
      languageDetails,
      projectDetails,
      skillDetails,
    };
    let fullNameCheck = validateFullName(full_name);
    let phoneCheck = validatePhone(phone_number);
    let emailCheck = validateEmail(email);
    let imageUrlCheck = validateImageUrl(image_url);
    let summaryCheck = validateSummary(summary);
    let addressCheck = validateAddress(address_line);
    let cityCheck = validateCity(city);
    let stateCheck = validateState(state);
    let countryCheck = validateCountry(country);
    let zipcodeCheck = validateZipcode(zipcode);
    let educationErrors = [];
    // iterating more than one educational details
    for (
      let educationData = 0;
      educationData < educationDetails.length;
      educationData++
    ) {
      let qualificationCheck = validateQualification(
        educationDetails[educationData].qualification
      );
      let coursenameCheck = validateCourseName(
        educationDetails[educationData].course_name
      );
      let instituteCheck = validateInstitute(
        educationDetails[educationData].institute
      );
      let instituteLocationCheck = validateInstituteLocation(
        educationDetails[educationData].institute_location
      );
      if (
        qualificationCheck !== "" ||
        coursenameCheck != "" ||
        instituteCheck !== "" ||
        instituteLocationCheck !== ""
      ) {
        educationErrors.push({
          index: educationData,
          qualificationError: qualificationCheck,
          courseNameError: coursenameCheck,
          instituteError: instituteCheck,
          instituteLocationError: instituteLocationCheck,
        });
      }
    }
    // if condition to check the form fields are empty or contain invalid data
    if (
      fullNameCheck != "" ||
      phoneCheck != "" ||
      emailCheck != "" ||
      imageUrlCheck != "" ||
      summaryCheck != "" ||
      addressCheck != "" ||
      cityCheck != "" ||
      stateCheck != "" ||
      countryCheck != "" ||
      zipcodeCheck !== "" ||
      educationErrors.length > 0
    ) {
      // it prevents the default form submission
      prevent_default();
      showError = true;
      showMessage = "Please fill in all required fields correctly";
      window.scrollTo(0, 0);
    } else {
      // API integration to update a resume
      try {
        const response = await fetch(
          `http://127.0.0.1:8000/update-resume/${editId}`,
          {
            method: "PUT",
            mode: "cors",
            cache: "no-cache",
            headers: {
              "Content-Type": "application/json",
            },
            // body: JSON.stringify(formValue)
            body: JSON.stringify(updateForm),
          }
        );

        const result = await response.json();
        console.log("Success:", result);
        successMessage = "Details updated successfully";
        window.scrollTo(0, 0);
        resetForm();
      } catch (error) {
        console.log("Error:", error);
        warningMessage = "Failed to update details. Please try again";
        window.scrollTo(0, 0);
      }
      console.log(updateForm);
    }
  }
</script>

<main>
  <nav>
    <div>
      <div class = "icon-style">
        <a href = "#/list">
          <Icon
            icon = "ri:arrow-left-s-line"
            width = "24"
            height = "24"
            color = "rgb(0,80,160)"
          /></a
        >
      </div>
      <div>
        <a href = "#/list" class = "link-style">Back to all Resume List</a>
      </div>
    </div>
  </nav>

  <form action = "" id = "formId" on:submit|preventDefault = {updateDetails}>
    {#if showError}
      <div class = "warning-alert">
        <!-- error messages if any fields are invalid -->
        <!-- svelte-ignore a11y-click-events-have-key-events -->
        <!-- svelte-ignore a11y-no-static-element-interactions -->
        <span class = "closebtn" on:click = {() => (showError = false)}
          >&times;</span
        >
        <!-- svelte-ignore missing-declaration -->
        <p class = "warning-msg">{showMessage}</p>
      </div>
    {/if}

    <!-- svelte-ignore missing-declaration -->
    {#if warningMessage != ""}
      <div class = "warning-alert">
        <!-- error messages if any fields are invalid -->
        <!-- svelte-ignore a11y-click-events-have-key-events -->
        <!-- svelte-ignore a11y-no-static-element-interactions -->
        <span class = "closebtn" on:click = {() => (warningMessage = "")}
          >&times;</span
        >
        <!-- svelte-ignore missing-declaration -->
        <p class = "warning-msg">{warningMessage}</p>
      </div>
    {/if}

    {#if successMessage != ""}
      <!-- svelte-ignore missing-declaration -->
      <div class="success-alert">
        <!-- error messages if any fields are invalid -->
        <!-- svelte-ignore a11y-click-events-have-key-events -->
        <!-- svelte-ignore a11y-no-static-element-interactions -->
        <span class="msg-closebtn" on:click={() => (successMessage = "")}
          >&times;</span
        >
        <!-- svelte-ignore missing-declaration -->
        <p class="success-msg">{successMessage}</p>
      </div>
    {/if}

    <h1 class="form-title">Edit Resume Page</h1>
    <!-- bind the data variables -->
    <PersonalDetails
      bind:full_name
      bind:email
      bind:phone_number
      bind:image_url
      bind:summary
    />
    <AddressDetails
      bind:address_line
      bind:street_name
      bind:city
      bind:state
      bind:country
      bind:zipcode
    />
    <EducationDetails bind:educationDetails />
    <WorkExperienceDetails bind:workExperienceDetails />
    <SkillsDetails bind:skillDetails />
    <SocialMediaDetails bind:socialMediaDetails />
    <ProjectDetails bind:projectDetails />
    <LanguageDetails bind:languageDetails />

    <!-- Save and Cancel Buttons -->
    <div class="formButtons">
      <ButtonInput
        buttonClass="save-button"
        type="submit"
        on:click={updateDetails}
        label="Save"
      />
      <a href="#/list"
        ><ButtonInput
          buttonClass="cancel-button"
          type="button"
          label="Cancel"
        /></a
      >
    </div>
  </form>
</main>

<style>
  .form-title {
    background-color: #f4f6f8;
    border-width: 4px;
    border-radius: 0.5rem;
    border-radius: 0.125rem;
    padding: 16px;
    font-family: "Times New Roman", Times, serif;
  }
  .formButtons {
    display: flex;
    justify-content: end;
  }
  .icon-style {
    position: absolute;
  }
  .link-style {
    margin-left: 23px;
    font-size: 20px;
  }
  /* error message styling */
  .warning-msg {
    color: #ff3860;
    font-size: 12px;
    height: 13px;
    margin-left: 6px;
  }
  .warning-alert {
    padding: 8px;
    background-color: #ffe4e1;
    color: rgb(0, 0, 0);
    margin-bottom: 15px;
    text-align: center;
    width: 98%;
    margin-top: 9px;
  }
  .success-msg {
    color: #001f02;
    font-size: 12px;
    height: 13px;
    margin-left: 6px;
  }
  .success-alert {
    padding: 8px;
    background-color: #c8fcd3;
    color: rgb(0, 0, 0);
    margin-bottom: 15px;
    text-align: center;
    width: 98%;
    margin-top: 9px;
  }
  /* close button for message */
  .closebtn {
    margin-left: 15px;
    color: rgb(0, 0, 0);
    font-weight: bold;
    float: right;
    font-size: 22px;
    line-height: 20px;
    cursor: pointer;
    transition: 0.3s;
  }
  .msg-closebtn {
    margin-left: 15px;
    color: rgb(0, 0, 0);
    font-weight: bold;
    float: right;
    font-size: 22px;
    line-height: 20px;
    cursor: pointer;
    transition: 0.3s;
  }
</style>

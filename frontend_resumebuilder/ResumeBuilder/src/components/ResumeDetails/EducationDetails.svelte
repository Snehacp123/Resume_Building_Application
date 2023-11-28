<script>
  // Import components and transition
  import DateInput from "../FormInputs/DateInput.svelte";
  import TextInput from "../FormInputs/TextInput.svelte";
  import { slide } from "svelte/transition";
  // Define an icon component using Iconify
  import Icon from "@iconify/svelte";
  // Import validation functions
  import {
    validateQualification,
    validateCourseName,
    validateInstitute,
    validateInstituteLocation,
    validateStartDate,
    validateEndDate

  } from "../../assets/js/validation";

  // Define data variables for education form
  export let educationDetails = [
    {
      qualification : "",
      course_name : "",
      institute : "",
      institute_location : "",
      academic_start_date : "",
      academic_end_date : "",
    },
  ];
  //Toggle state for accordion
  export let open = false;
  // Function to handle accordion toggle
  const handleClick = () => (open = !open);

  // Function to add a new education field
  const addNewEducation = () => {
    educationDetails = [
      ...educationDetails,
      {
        qualification : "",
        course_name : "",
        institute : "",
        institute_location : "",
        academic_start_date : "",
        academic_end_date : "",
      },
    ];
  };
  // Function to remove an education field
  const removeEducation = (index) => {
    if (educationDetails.length > 1) {
      educationDetails = educationDetails.filter((_, entry) => entry !== index);
    }
  };
</script>

<main>
  <div class="educationContent">
    <!-- svelte-ignore a11y-click-events-have-key-events -->
    <!-- svelte-ignore a11y-no-static-element-interactions -->
    <div class="accordion-class" on:click = {handleClick}>
      <h2 class="subHeading">Education</h2>
      <div class="icon-style">
        <!-- display the appropriate icon based on whether the accordion is open or closed -->
        {#if open}
          <Icon
            icon = "material-symbols:keyboard-arrow-up"
            width = "24"
            height = "24"
            color = "black"
          />
        {:else}
          <Icon
            icon = "material-symbols:keyboard-arrow-down"
            width = "24"
            height = "24"
            color ="black"
          />
        {/if}
      </div>
    </div>
    {#if open}
      {#each educationDetails as education, entry}
        <!-- slide transition to the accordion content when it is opened or closed -->
        <div class="active" transition:slide>
          <!-- two-way binding to the qualification data variable -->
          <TextInput
            placeholder = "Enter Qualification"
            label = "Qualification"
            id = "qualification"
            bind:value = {education.qualification}/>
          <!-- svelte-ignore missing-declaration -->
          <div class = "errors">
            {education.qualification &&
              validateQualification(education.qualification)}
          </div>
          <TextInput
            placeholder = "Enter Course Name"
            label = "Course Name"
            id = "course_name"
            bind:value = {education.course_name}/>
          <!-- svelte-ignore missing-declaration -->
          <div class = "errors">
            {education.course_name && validateCourseName(education.course_name)}
          </div>

          <TextInput
            placeholder = "Enter Institute Name"
            label = "Institute"
            id = "institute"
            bind:value = {education.institute}/>
          <!-- svelte-ignore missing-declaration -->
          <div class = "errors">
            {education.institute && validateInstitute(education.institute)}
          </div>

          <TextInput
            placeholder = "Enter Institute Location"
            label = "Institute Location"
            id = "institute_location"
            bind:value = {education.institute_location}/>
          <!-- svelte-ignore missing-declaration -->
          <div class = "errors">
            {education.institute_location &&
              validateInstituteLocation(education.institute_location)}
          </div>

          <DateInput
            placeholder = ""
            label = "Start Date"
            id = "academic_start_date"
            bind:value = {education.academic_start_date}/>
            <div class = "errors">
              {education.academic_start_date &&
                validateStartDate(education.academic_start_date)}
            </div>

          <DateInput
            placeholder = ""
            label = "End Date"
            id = "academic_end_date"
            bind:value = {education.academic_end_date}/>
            <div class = "errors">
              {education.academic_end_date &&
                validateEndDate(education.academic_end_date)}
            </div>

          <div class="multiple-fields">
            <div class = "add-new">
              <!-- svelte-ignore a11y-click-events-have-key-events -->
              <!-- svelte-ignore a11y-no-static-element-interactions -->
              <button on:click|preventDefault = {addNewEducation}>+ Add</button>
            </div>

            <div class = "remove-new">
              {#if entry != 0}
                <!-- svelte-ignore a11y-no-static-element-interactions -->
                <!-- svelte-ignore a11y-click-events-have-key-events -->
                <button on:click|preventDefault = {() => removeEducation(entry)}>- Remove</button>
              {/if}
            </div>
        </div>
        </div>
      {/each}
    {/if}
  </div>
</main>

<style>
  /* Style accordion heading on hover */
  h2:hover {
    cursor: pointer;
  }
  /* Style accordion container */
  .accordion-class {
    display: flex;
  }

  /* Position icon style */
  .icon-style {
    right: 20px;
    position: absolute;
    padding-top: 20px;
  }
  .subHeading {
    background-color: #ffffff;
    border-width: 4px;
    border-radius: 0.5rem;
    border-radius: 0.125rem;
    padding: 16px;
    width: 100%;
    box-shadow: inset 0px -1px 4px 0px rgba(0, 0, 0, 0.2);
    margin: 2px;
    font-family: 'Times New Roman', Times, serif;
  }
  .errors{
    color: #ff3860;
    font-size: 12px;
    margin-left: 6px;
  }
  .subHeading::after{
    content: " *";
    color: red;
    font-size: 20px;
}
  
  /* add  and remove button styling */
  button {
    margin-top: 5px;
    border-radius: 3px;
    color: #2890ff;
    background-color: #ffffff;
    font-size: 15px;
    padding: 6px;
    margin-right: 5px;
  }
  .multiple-fields{
    display: flex;
    padding-right: 2px;
  }
  @media (max-width: 500px){
    .subHeading {
      background-color: #ffffff;
      border-width: 4px;
      border-radius: 0.5rem;
      border-radius: 0.125rem;
      padding: 16px;
      width: 100%;
      box-shadow: inset 0px -1px 4px 0px rgba(0, 0, 0, 0.2);
      margin: 1px;
      font-family: 'Times New Roman', Times, serif;
      font-size: 35px;
  }
  }
</style>

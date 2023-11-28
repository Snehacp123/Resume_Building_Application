<script>
  // font-icon
  import Icon from "@iconify/svelte";
  import DateInput from "../FormInputs/DateInput.svelte";
  import TextInput from "../FormInputs/TextInput.svelte";
  export let open = false;
  import { slide } from "svelte/transition";

  const handleClick = () => (open = !open);
  export let workExperienceDetails = [
    {
      job_title: "",
      organization: "",
      key_roles: "",
      job_location: "",
      job_start_date: "",
      job_end_date: "",
    },
  ];

  const addWorkExperience = () => {
    workExperienceDetails = [
      ...workExperienceDetails,
      {
        job_title: "",
        organization: "",
        key_roles: "",
        job_location: "",
        job_start_date: "",
        job_end_date: "",
      },
    ];
  };
  const removeWorkExperience = (index) => {
    if (workExperienceDetails.length > 1) {
      workExperienceDetails = workExperienceDetails.filter(
        (_, entry) => entry !== index
      );
    }
  };
</script>

<main>
  <div class = "workContent">
    <!-- svelte-ignore a11y-click-events-have-key-events -->
    <!-- svelte-ignore a11y-no-static-element-interactions -->
    <div class = "accordion-class" on:click = {handleClick}>
      <h2 class = "subHeading">Work Experience</h2>
      <div class = "icon-style">
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
            color = "black"
          />
        {/if}
      </div>
    </div>
    {#if open}
      {#each workExperienceDetails as workexperience, entry}
        <div class = "active" transition:slide>
          <TextInput
            placeholder = "Enter Job Title"
            label = "Job Title"
            id = "job-title"
            bind:value = {workexperience.job_title}
          />
          <TextInput
            placeholder = "Enter Organization"
            label = "Organization"
            id = "organization"
            bind:value = {workexperience.organization}/>
          <TextInput
            placeholder = "Enter Job location"
            label = "Job Location"
            id = "job-location"
            bind:value = {workexperience.job_location}/>
          <TextInput
            placeholder = "Enter Key Roles"
            label = "Key Roles"
            id = "key_roles"
            bind:value = {workexperience.key_roles}/>

          <DateInput
            placeholder = ""
            label = "Start Date"
            id = "job_start_date"
            bind:value = {workexperience.job_start_date}/>
          <DateInput
            placeholder = ""
            label = "End Date"
            id = "job_end_date"
            bind:value = {workexperience.job_end_date}/>
            <div class="multiple-fields">
                <div class = "add-new">
                    <button on:click|preventDefault = {addWorkExperience}>+ Add</button>
                </div>

                <div class = "remove-work">
                    {#if entry != 0}
                    <button on:click|preventDefault = {() => removeWorkExperience(entry)}>- Remove</button>
                    {/if}
                </div>
            </div>
        </div>
      {/each}
    {/if}
  </div>
</main>

<style>
  h2:hover {
    cursor: pointer;
  }
  .accordion-class {
    display: flex;
  }
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
    font-family: "Times New Roman", Times, serif;
  }
  button {
    margin-top: 5px;
    border-radius: 3px;
    color: #2890ff;
    background-color: #ffffff;
    font-size: 15px;
    padding: 8px;
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

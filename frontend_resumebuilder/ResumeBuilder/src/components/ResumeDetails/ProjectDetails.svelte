<script>
  // Import components and transition
  import TextInput from "../FormInputs/TextInput.svelte";
  import Icon from "@iconify/svelte";
  import { slide } from "svelte/transition";

  // Define data variables for project form
  export let projectDetails = [
    { 
      project_name: "", 
      skills_earned: "", 
      project_description: "" 
    }
  ];

  //Toggle state for accordion
  export let open = false;
  // Function to handle accordion toggle
  const handleClick = () => (open = !open);

  // Function to add a new project field
  const addProject = () => {
    projectDetails = [
      ...projectDetails,
      { 
        project_name: "", 
        skills_earned: "", 
        project_description: "" 
      }
    ];
  };
  // Function to remove an project field
  const removeProject = (index) => {
    if (projectDetails.length > 1) {
      projectDetails = projectDetails.filter((_, entry) => entry !== index);
    }
  };
</script>

<main>
  <div class = "projectContent">
    <!-- svelte-ignore a11y-click-events-have-key-events -->
    <!-- svelte-ignore a11y-no-static-element-interactions -->
    <div class = "accordion-class" on:click = {handleClick}>
      <h2 class = "subHeading">Project</h2>
      <div class = "icon-style">
        {#if open}
          <Icon
            icon = "material-symbols:keyboard-arrow-up"
            width = "24"
            height = "24"
            color = "black"/>
        {:else}
          <Icon
            icon = "material-symbols:keyboard-arrow-down"
            width = "24"
            height = "24"
            color = "black"/>
        {/if}
      </div>
    </div>
    {#if open}
      {#each projectDetails as project, entry}
        <div class = "active" transition:slide>
            <TextInput
              placeholder = "Enter Project Name"
              label = "Project Name"
              id = "project_name"
              bind:value = {project.project_name}/>
            <TextInput
              placeholder = "Enter Skills Earned"
              label = "Skills Earned"
              id = "skills_earned"
              bind:value = {project.skills_earned}/>
            <TextInput
              placeholder = "Project Description"
              label = "Project Description"
              id = "project_description"
              bind:value = {project.project_description}/>
              <div class="multiple-fields">
                <div class = "add-new">
                  <button on:click|preventDefault = {addProject}>+ Add</button>
                </div>

                <div class = "remove-new">
                  {#if entry !=  0}
                    <button on:click|preventDefault = {() => removeProject(entry)}>- Remove</button>
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
    font-family: 'Times New Roman', Times, serif;
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

<script>
  // Import components and transition
  import Icon from "@iconify/svelte";
  import TextInput from "../FormInputs/TextInput.svelte";
  import SelectInput from "../FormInputs/SelectInput.svelte";
  import { slide } from "svelte/transition";

  // Define data variables for skill form
  export let selectSkillLevel = [
    "Expert",
    "Advanced",
    "Intermediate",
    "Beginner",
  ];
  export let skillDetails = [{ skill_name: "", skill_level: "" }]; // Array to store the list of skills and skill levels
  //Toggle state for accordion
  export let open = false;
  // Function to handle accordion toggle
  const handleClick = () => (open = !open);

  // Function to add a new skill field
  const addNewSkill = () => {
    skillDetails = [...skillDetails, { skill_name: "", skill_level: "" }];
  };
  // Function to remove an education field
  const removeSkill = (index) => {
    if (skillDetails.length > 1) {
      skillDetails = skillDetails.filter((_, entry) => entry !== index);
    }
  };
</script>

<main>
  <div class = "skillContent">
    <!-- svelte-ignore a11y-click-events-have-key-events -->
    <!-- svelte-ignore a11y-no-static-element-interactions -->
    <div class = "accordion-class" on:click = {handleClick}>
      <h2 class = "subHeading">Skills</h2>
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
      {#each skillDetails as skill, entry}
        <div class = "active" transition:slide>
          <TextInput
            placeholder = "Enter Skills"
            label = "Skills"
            id = "skill_name"
            bind:value = {skill.skill_name}/>
          <SelectInput
            label = "Skill Level"
            options = {selectSkillLevel}
            defaultOption = "select your current skill level"
            bind:value = {skill.skill_level}/>
            <div class = "multiple-fields">
              <div class = "add-new">
                <button on:click|preventDefault = {addNewSkill}>+ Add</button>
              </div>

              <div class = "remove-new">
                {#if entry != 0}
                  <button on:click|preventDefault = {() => removeSkill(entry)}>- Remove</button>
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

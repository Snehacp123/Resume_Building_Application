<script>
  // Import components and transition
  import TextInput from "../FormInputs/TextInput.svelte";
  import SelectInput from "../FormInputs/SelectInput.svelte";
  import { slide } from "svelte/transition";
  // Define an icon component using Iconify
  import Icon from "@iconify/svelte";
  
  export let selectLanguageProficiency = [
    "Expert",
    "Advanced",
    "Intermediate",
    "Beginner",
  ];
  export let languageDetails = [{ language: "", proficiency: "" }];

  //Toggle state for accordion
  export let open = false;
  // Function to handle accordion toggle
  const handleClick = () => (open = !open);
  // Function to add a new language field
  const addNewLanguage = () => {
    languageDetails = [...languageDetails, { language: "", proficiency: "" }];
  };
  // Function to remove an language field
  const removeLanguage = (index) => {
    if (languageDetails.length > 1) {
      languageDetails = languageDetails.filter((_, entry) => entry !== index);
    }
  };
</script>

<main>
  <div class="languageContent">
    <!-- svelte-ignore a11y-click-events-have-key-events -->
    <!-- svelte-ignore a11y-no-static-element-interactions -->
    <div class="accordion-class" on:click={handleClick}>
      <h2 class="subHeading">Language</h2>
      <div class="icon-style">
        <!-- display the appropriate icon based on whether the accordion is open or closed -->
        {#if open}
          <Icon
            icon="material-symbols:keyboard-arrow-up"
            width="24"
            height="24"
            color="black"
          />
        {:else}
          <Icon
            icon="material-symbols:keyboard-arrow-down"
            width="24"
            height="24"
            color="black"
          />
        {/if}
      </div>
    </div>
    {#if open}
      {#each languageDetails as language, entry}
        <!-- slide transition to the accordion content when it is opened or closed -->
        <div class = "active" transition:slide>
          <TextInput
            label = "Language"
            id = "language"
            placeholder = "Language"
            bind:value = {language.language}/>
          <SelectInput
            label = "Proficiency"
            options = {selectLanguageProficiency}
            defaultOption = "select your language proficiency"
            bind:value = {language.proficiency}/>
          <div class = "multiple-fields">  
            <div class = "add-new">
              <button on:click|preventDefault = {addNewLanguage}>- Add</button>
            </div>

            <div class = "remove-new">
              {#if entry != 0}
                <button on:click|preventDefault = {() => removeLanguage(entry)}>- Remove</button>
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
  
  /* add  and remove button styling */
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

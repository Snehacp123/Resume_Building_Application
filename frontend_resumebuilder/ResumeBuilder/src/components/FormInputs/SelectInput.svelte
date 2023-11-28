<script>
  // Exporting the properties for the select input component
  // These properties used to customize the appearence and behavior of the select fields
  export let defaultOption = "";
  export let options = [];
  export let label = "";
  export let id = "";
  export let value = "";
</script>

<main>
  <div class = "selectInput">
    <div class = "labelField">
      <!-- Label for the select input -->
      <label for = {id}>{label}</label>
    </div>
    <div class = "selectField">
      <!-- Select input element -->
      <select bind:value>
        <!-- Default option -->
        <option value = "">{defaultOption}</option>
        <!-- Looping through the options array -->
        {#each options as option}
          <!-- Creating an option for each item in the array -->
          <option value = {option}>{option}</option>
        {/each}
      </select>
    </div>
  </div>
</main>

<style>
  /* Styling for the select input component */
  .selectInput {
    display: flex;
    border: solid 1px rgb(207, 203, 203);
    height: 43px;
  }
  /* Styling for the select label */
  .labelField {
    width: 20%;
    background-color: #f4f6f8;
  }
  label {
    padding-left: 13px;
    padding-top: 10px;
  }
  .selectField {
    width: 40%;
  }
  select {
    width: 100%;
    border: none;
    border-bottom: 2px solid #ffefef;
    padding: 9px;
    margin-left: 4px;
    font-size: 1em;
    background-color: white;
    outline: none;
    font-family: 'Times New Roman', Times, serif;
  }
  select:hover {
    border-bottom: 2px solid teal;
    outline: #ffffff;
  }
  /* this hides the default option*/
  select option:first-child {
    display: none;
  }
  /* to modify the styles for smaller screens */
  @media (max-width: 500px){
    .labelField{
      display: none;
    }
    .selectField {
      width: 100%;
    }
    select {
      font-size: 20px;
    }
  }
</style>

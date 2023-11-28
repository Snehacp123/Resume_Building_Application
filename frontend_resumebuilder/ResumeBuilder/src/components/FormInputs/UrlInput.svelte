<script>
  // Exporting the properties for the url input component
  // These properties used to customize the appearence and behavior of the url input field
  export let id = "";
  export let placeholder = "";
  export let label = "";
  export let value;
</script>

<main>
  <div class = "inputContent">
    <div class = "labelField">
      <!-- Label for the input field -->
      <label for = {id}>{label}</label>
    </div>
    <div class = "inputField">
      <!-- url input element -->
      <input type = "url" {id} {placeholder} bind:value />
    </div>
  </div>
</main>

<style>
  .inputContent {
    /* Styling for the input content */
    display: flex;
    border: solid 1px rgb(207, 203, 203);
    height: 43px;
  }
  /* Styling for the label */
  .labelField {
    width: 20%;
    background-color: #f4f6f8;
  }
  label {
    padding-left: 13px;
    padding-top: 10px;
    font-family: 'Times New Roman', Times, serif;
  }
  /* Styling for the url input component */
  .inputField {
    width: 40%;
  }
  input[type="url"] {
    width: 100%;
    border: none;
    border-bottom: 2px solid #ffefef;
    padding: 9px;
    margin-left: 4px;
    font-size: 1em;
    outline: none;
    font-family: 'Times New Roman', Times, serif;
  }
  /* changes the border color when the input field is hovered over. */
  input:hover {
    border-bottom: 2px solid teal;
    outline: #ffffff;
  }
  /* to modify the styles for smaller screens */
  @media (max-width: 500px){
    .labelField{
      display: none;
    }
    .inputField {
      width: 100%;
    }
    input[type="url"] {
      font-size: 20px;
    }
  }
</style>

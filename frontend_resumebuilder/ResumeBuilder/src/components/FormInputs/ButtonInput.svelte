<script>
  // Exporting the properties for the button component
  // These properties used to customize the appearence and behavior of the button
  export let buttonClass = "";
  export let type = "";
  export let label = "";
</script>

<main>
  <div class="button-container">
    <!-- Button element with dynamic class, type, and label -->
    <button class = {buttonClass} {type}> {label} </button>
  </div>
</main>

<style>
  /* Styling for the button container */
  .button-container {
    margin-top: 20px;
  }
  /* Styling for the save button */
  .save-button {
    background-color: #2890ff;
    color: white;
    padding: 10px 20px;
    font-size: 16px;
    font-weight: bold;
    width: 100px;
    margin-right: 12px;
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    margin-left: 10px;
  }
  /* Styling for the cancel button */
  .cancel-button {
    background-color: #f3f3f3;
    color: teal;
    padding: 10px 20px;
    font-size: 16px;
    font-weight: bold;
    width: 100px;
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
  }
  /* to modify the styles for smaller screens */
  @media (max-width : 500px){
    .save-button {
    background-color: #2890ff;
    color: white;
    padding: 10px 20px;
    font-size: 24px;
    font-weight: bold;
    width: 100%;
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    margin-left: 2px;
    height: 65px;
    margin-bottom: 0px;
    
  }
  .cancel-button {
    background-color: #f3f3f3;
    color: teal;
    padding: 10px 20px;
    font-size: 24px;
    font-weight: bold;
    width: 100%;
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    height: 65px;
  }
  }
</style>

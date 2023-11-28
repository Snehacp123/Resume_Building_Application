<script>
  // Import components and transition
  import TextInput from "../FormInputs/TextInput.svelte";
  import SelectInput from "../FormInputs/SelectInput.svelte";
  import { slide } from "svelte/transition";
  // Define an icon component using Iconify
  import Icon from "@iconify/svelte";
  // Import validation functions
  import {
    validateAddress,
    validateCountry,
    validateState,
    validateCity,
    validateZipcode
  } from "../../assets/js/validation";

  // Define data variables for address form
  export let address_line = "";
  export let street_name = "";
  export let city = "";
  export let state = "";
  export let country = "";
  export let zipcode = "";
  export let selectCountry = [
    "India",
    "United States",
    "Canada",
    "Germany",
    "China",
  ];
  // Toggle state for accordion
  export let open = false;
  // Function to handle accordion toggle
  const handleClick = () => (open = !open);

</script>

<main>
  <div class="addressContent">
    <!-- svelte-ignore a11y-click-events-have-key-events -->
    <!-- svelte-ignore a11y-no-static-element-interactions -->
    <!-- event listener to handle the accordion toggle -->
    <div class = "accordion-class" on:click = {handleClick}>
      <h2 class = "subHeading">Address</h2>
      <div class = "icon-style">
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
            color = "black"
          />
        {/if}
      </div>
    </div>
    {#if open}
    <!-- slide transition to the accordion content when it is opened or closed -->
      <div class = "active" transition:slide>
        <!-- two-way binding to the address_line data variable. -->
        <div class="requred">
        <TextInput
          placeholder = "Enter Address"
          label = "Address Line"
          id = "address"
          bind:value = {address_line}
        /></div>
        <!--
           display an error message if the address line is invalid. 
           The && operator ensures that the error message is only displayed if the address line is not empty.
        -->
        <div class = "errors">
          {address_line && validateAddress(address_line)}
        </div>
        <TextInput
          placeholder = "Enter Street Name"
          label = "Street Name"
          id = "street-ame"
          bind:value = {street_name}
        />
        <TextInput
          placeholder = "Enter City"
          label = "City"
          id = "city"
          bind:value = {city}
        />
        <div class = "errors">{city && validateCity(city)}</div>
        <TextInput
          placeholder = "Enter State"
          label = "state"
          id = "state"
          bind:value = {state}
        />
        <div class = "errors">{state && validateState(state)}</div>
        <SelectInput
          label = "Country"
          options = {selectCountry}
          defaultOption = "Choose your country"
          bind:value = {country}
        />
        <div class = "errors">{country && validateCountry(country)}</div>
        <TextInput
          placeholder = "Enter Zipcode"
          label = "Zipcode"
          id = "zipcode"
          bind:value = {zipcode}
        />
        <div class = "errors">{zipcode && validateZipcode(zipcode)}</div>
      </div>
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
  /* styling for heading */
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
  }
  /* styling for error messages */
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

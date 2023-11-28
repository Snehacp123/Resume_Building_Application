<script>
  // Import components and transition
  import EmailInput from "../FormInputs/EmailInput.svelte";
  import TextInput from "../FormInputs/TextInput.svelte";
  import UrlInput from "../FormInputs/UrlInput.svelte";
  import { slide } from "svelte/transition";
  // Define an icon component using Iconify
  import Icon from "@iconify/svelte";
  
  // Import validation functions
  import {
    validateEmail,
    validateFullName,
    validateImageUrl,
    validatePhone,
    validateSummary,
  } from "../../assets/js/validation";

  // Define data variables for education form
  export let full_name = "";
  export let email = "";
  export let phone_number = "";
  export let image_url = "";
  export let summary = "";
  //Toggle state for accordion
  export let open = false;
  // Function to handle accordion toggle
  const handleClick = () => (open = !open);
</script>

<main>
  <div class = "personalContent">
    <!-- svelte-ignore a11y-click-events-have-key-events -->
    <!-- svelte-ignore a11y-no-static-element-interactions -->
    <div class = "accordion-class" on:click = {handleClick}>
      <h2 class = "subHeading">Basic</h2>
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
      <div class = "active" transition:slide>
        <TextInput
          placeholder = "Enter your Full Name"
          label = "Name"
          id = "full_name"
          bind:value = {full_name}/>
        <div class = "errors">{full_name && validateFullName(full_name)}</div>

        <EmailInput
          placeholder = "Enter your Email"
          label = "Email"
          id = "email"
          bind:value = {email}/>
        <div class = "errors">{email && validateEmail(email)}</div>

        <TextInput
          placeholder = "Enter your Phone Number"
          label = "Phone Number"
          id = "phone_number"
          bind:value = {phone_number}/>
        <div class = "errors">{phone_number && validatePhone(phone_number)}</div>

        <UrlInput
          placeholder = "Enter Image URL"
          label = "Image URL"
          id = "image_url"
          bind:value = {image_url}/>
        <div class = "errors">{image_url && validateImageUrl(image_url)}</div>

        <TextInput
          placeholder = "Summary"
          label = "Summary"
          id = "summary"
          bind:value = {summary}/>
        <div class = "errors">{summary && validateSummary(summary)}</div>
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

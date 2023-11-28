<script>
  // Import components and transition
  import Icon from "@iconify/svelte";
  import TextInput from "../FormInputs/TextInput.svelte";
  import { slide } from "svelte/transition";

  // Function to handle accordion toggle
  export let open = false;
  const handleClick = () => (open = !open);

  // Define data variables for socialmedia form
  export let socialMediaDetails = [{ network: "", username: "", url: "" }];

  // Function to add a new socialmedia field
  const addNewSocialMedia = () => {
    socialMediaDetails = [
      ...socialMediaDetails,
      { network: "", username: "", url: "" },
    ];
  };
  // Function to remove an socialmedia field
  const removeSocialMedia = (index) => {
    if (socialMediaDetails.length > 1) {
      socialMediaDetails = socialMediaDetails.filter((_, entry) => entry !== index);
    }
  };
</script>

<main>
  <div class = "socialMediaContent">
    <!-- svelte-ignore a11y-click-events-have-key-events -->
    <!-- svelte-ignore a11y-no-static-element-interactions -->
    <div class = "accordion-class" on:click = {handleClick}>
      <h2 class = "subHeading">Social Media</h2>
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
            color = "black"/>
        {/if}
      </div>
    </div>
    {#if open}
      {#each socialMediaDetails as social_media, entry}
        <div class = "active" transition:slide>
          <TextInput
            placeholder = "Enter Network"
            label = "Network"
            id = "network"
            bind:value = {social_media.network}/>
          <TextInput
            placeholder = "Enter Username"
            label = "Username"
            id = "username"
            bind:value = {social_media.username}/>
          <TextInput
            placeholder = "Enter URL"
            label = "URL"
            id = "url"
            bind:value = {social_media.url}/>
            <div class="multiple-fields">
              <div class = "add-new">
                <button on:click|preventDefault = {addNewSocialMedia}>+ Add</button>
              </div>

              <div class = "remove-new">
                {#if entry != 0}
                  <button on:click|preventDefault = {() => removeSocialMedia(entry)}>- Remove</button>
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

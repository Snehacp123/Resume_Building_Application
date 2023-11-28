<script>
  // import necessary components
  import Icon from "@iconify/svelte";

  // function to cancel the delete confirmation
  function cancelDeleteConfirmation() {
    openDeleteConfirmation = false;
  }

  // updating a resume
  export let editId = "";
  function updateResume(id){
    editId = id;
    // console.log(editId);
    window.history.pushState({editId}, null, "#/edit");
    document.location.reload();
    dispatchEvent(new Event('popstate'))
  }

  //showing the delete confirmation box
  export let deleteId;
  export let openDeleteConfirmation = false;
  function showDeleteConfirmation(id) {
    openDeleteConfirmation = !openDeleteConfirmation;
    deleteId = id;
    console.log(deleteId);
  }

  // toggling the display of edit and delete options
  let showOptions = false;
  let selectedId = null;
  function toggleOptions(id) {
      showOptions = !showOptions;
      selectedId = id;
  }

  // API call to fetch all resume from the API
  let data = [];
  async function fetchResumes() {
    const response = await fetch("http://127.0.0.1:8000/resumes");
    const parsedData = await response.json();
    data = parsedData;
  }
  fetchResumes();

  //API call to delete a resume entry
  function apiDeleteFunction() {
    fetch(`http://127.0.0.1:8000/delete-resume/${deleteId}`, {
      method: "DELETE",
    })
      .then((response) => response.json())
      .then((data) => console.log(data));
    open = false;
    window.location.reload();
  }

  // API call to fetch resume using email, name and phone number
  let entryData = "";
  let allDetails = null;
  async function apiSearchResume(entryData) {
    if (entryData.trim() !== "") {
      const response = await fetch(
        `http://127.0.0.1:8000/search-resume/${entryData}`,
        {
          method: "GET",
        }
      );
      allDetails = await response.json();
      console.log(allDetails);
    } else {
      allDetails = null;
    }
  }

</script>

<main>
  {#if openDeleteConfirmation}
    <!-- svelte-ignore a11y-click-events-have-key-events -->
    <!-- svelte-ignore a11y-no-static-element-interactions -->
    <div class = "delete-page" on:click = {cancelDeleteConfirmation}>
      <div class = "container">
        <p class = "title">Delete Entry</p>
        <p class = "message">Are you sure you want to delete?</p>
        <div class = "button-container">
          <button class = "btn-cancel" on:click = {cancelDeleteConfirmation}>Cancel</button>
          <button class = "btn-delete" on:click = {apiDeleteFunction}>Yes, Delete</button>
        </div>
      </div>
    </div>
  {/if}

  <div class = "listingpage-title">
    <h1>Resumes</h1>
  </div>
  <hr/>
  <div class = "link-style">
    <div class = "search-bar">
      <input
        type = "search"
        id = "search"
        placeholder = "Search by name, phno or email"
        bind:value = {entryData}/>
      <!-- svelte-ignore a11y-no-static-element-interactions -->
      <!-- svelte-ignore a11y-click-events-have-key-events -->
      <div class = "search-icon" on:click = {apiSearchResume(entryData)}>
        <Icon
          icon = "material-symbols:search"
          width = "24"
          height = "24"
          color = "black"/>
      </div>
    </div>
    <div class = "add-icon">
      <div class = "icon-style"><a href="#/">
        <Icon
          icon = "material-symbols:add"
          width = "24"
          height = "24"
          color = "rgb(0,80,160)"/></a>
      </div>
      <div class = "link-title">
        <a href = "#/" class = "link-style">Add New Resume</a>
      </div>
    </div>
  </div>

  <table class = "table">
    <thead>
      <tr>
        <th>ID</th>
        <th>Name</th>
        <th>Email</th>
        <th>Phone</th>
        <th></th>
      </tr>
    </thead>
    <!-- for listing the searched resume details -->
    {#if allDetails !== null}
      {#each allDetails as data}
      <tbody>
        <tr>
          <td>{data.id}</td>
          <td>{data.full_name}</td>
          <td>{data.email}</td>
          <td>{data.phone_number}</td>
          <td>
            <!-- svelte-ignore a11y-click-events-have-key-events -->
            <!-- svelte-ignore a11y-no-static-element-interactions -->
            <div on:click = {() => toggleOptions(data.id)}>
              <Icon
                icon = "charm:menu-kebab"
                width = "24"
                height = "24"
                color = "black"
              />
            </div>
            {#if showOptions && selectedId === data.id}
              <div class = "options">
                <!-- svelte-ignore missing-declaration -->
                <button
                  on:click = {() => {
                    showOptions = false; updateResume(data.id);}}>Edit
                    </button>
                <button
                  on:click = {() => {
                    showOptions = false;
                    showDeleteConfirmation(data.id);}}>Delete</button>
              </div>
            {/if}
          </td>
        </tr>
      </tbody>
      {/each}
    {:else}
      {#each Object.entries(data) as [key, value]}
        <tbody>
          <tr>
            <!-- <td>{generateSerialNumber(index)}</td> -->
            <td>{value.id}</td>
            <td>{value.full_name}</td>
            <td>{value.email}</td>
            <td>{value.phone_number}</td>

            <!-- svelte-ignore a11y-click-events-have-key-events -->
            <td>
              <!-- svelte-ignore a11y-no-static-element-interactions -->
              <div on:click = {() => toggleOptions(value.id)}>
                <Icon
                  icon = "charm:menu-kebab"
                  width = "24"
                  height = "24"
                  color = "black"
                />
              </div>
              {#if showOptions && selectedId === value.id}
                <div class = "options">
                  <!-- svelte-ignore missing-declaration -->
                  <button
                  on:click = {() => {
                    showOptions = false; updateResume(value.id);}}>
                    Edit</button>
                    
                  <button
                    on:click={() => {
                      showOptions = false;
                      showDeleteConfirmation(value.id);}}>Delete</button>
                </div>
              {/if}
            </td>
          </tr>
        </tbody>
      {/each}
    {/if}
  </table>
  
</main>

<style>
  /* Style the table to have a width of 100% */
  table {
    width: 100%;
  }
  /* Style the search bar container */
  .search-bar {
    margin-bottom: 1em;
    margin-top: 0%;
    padding-right: 538px;
    justify-content: left;
    align-items: left;
    display: flex;
  }
  /* Style the search input field */
  .search-bar input {
    width: 100%;
    border: 1px solid #ccc;
    padding: 0.5em;
  }
  /* Style the table to have borders and collapse rows */
  .table {
    border-collapse: collapse;
    width: 100%;
  }
  .link-style{
    color: blue;
  }

  /* Style the table headers and table cells to have padding */
  .table th,
  .table td {
    padding: 0.5em;
  }

  .table th {
    background-color: #eee;
    text-align: left;
  }

  .table tr:hover {
    background-color: #f5f5f5;
  }
  /* style the search option */
  .search-icon {
    padding-top: 5px;
  }
  .search-bar {
    display: flex;
  }
  .search-icon {
    border: 1px solid #ccc;
    height: 29px;
    background-color: #ebeaea;
  }
  .add-icon {
    display: flex;
  }
  /* add space between search bar and add new resume link */
  .link-style {
    justify-content: space-between;
    text-align: right;
    display: flex;
  }
  .link-title {
    font-size: 20px;
  }
  h1 {
    margin: 0%;
  }
  /* style the edit and delete options */
  .options {
    display: flex;
    flex-direction: column;
    position: absolute;
    background-color: white;
    border: 1px solid #ccc;
    padding: 0.5em;
    z-index: 1;
  }
  .options button {
    margin-bottom: 0.5em;
  }
  .listingpage-title {
    background-color: #f4f6f8;
    border-width: 4px;
    border-radius: 0.5rem;
    border-radius: 0.125rem;
    padding: 16px;
    font-family: "Times New Roman", Times, serif;
    margin: 0px;
  }
  .delete-page {
    height: 100%;
    background: rgba(0, 0, 0, 0.8);
    width: 100%;
    position: fixed;
  }
  .title {
    background-color: #fce9e2;
    color: #000000;
    padding: 10px;
    margin: 0px;
  }
  .container {
    width: 50%;
    padding: 1px;
    left: 0;
    margin-left: 25%;
    border: 1px solid #ccc;
    border-radius: 10px;
    position: absolute;
    top: 15%;
    box-shadow: 5px 5px 5px #000;
    background-color: #fff;
    justify-content: center;
  }
  .btn-delete {
    background-color: teal;
    color: #fff;
    border: none;
    padding: 10px 20px;
    margin: 10px;
    border-radius: 5px;
    cursor: pointer;
  }
  /* Cancel button styles */
  .btn-cancel {
    background-color: #e2e2e2;
    color: teal;
  }
  .button-container {
    text-align: center;
    justify-content: center;
  }
  p {
    text-align: center;
  }
  a {
    text-decoration: none;
    color: #000;
  }
</style>

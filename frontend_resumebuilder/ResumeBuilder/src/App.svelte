<script>
    import Router from "svelte-spa-router";
    import ResumeForm from "./components/ResumeDetails/ResumeForm.svelte";
    import ListingPageDetails from "./components/ListingPage/ListingPageDetails.svelte";
    import EditResumeDetails from "./components/EditPage.svelte/EditResumeDetails.svelte";
    //maps URLs to corresponding components. 
    let routes = {
        "/": ResumeForm,
        "/list": ListingPageDetails,
        "/edit": EditResumeDetails,
    }
</script>

<main>
    
    <Router {routes}/>
    
</main>

<style>

</style>
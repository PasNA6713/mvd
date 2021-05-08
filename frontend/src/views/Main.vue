<template>
  <div>
    <Header />
    <Navbar />
    <router-view style="margin-bottom: 60px"/>
    <Footer />
  </div>
</template>

<script>
import Header from "@/components/main/Header.vue";
import Footer from "@/components/main/Footer.vue";
import Navbar from "@/components/main/Navbar.vue";

export default {
  name: "Main",
  components: {
    Header,
    Footer,
    Navbar,
  },
};
</script>
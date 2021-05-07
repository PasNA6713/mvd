<template>
  <div>
     <SMdialog />
  </div>
</template>

<style lang="scss" scoped> 
@import '@/styles/common.scss';
@import '@/styles/views/stat.scss';
</style>

<script>
import Navbar from "@/components/Navbar.vue"
import Header from "@/components/Header.vue"
import SMdialog from "@/components/SMdialog.vue"


export default {
  name: 'Social',
  components: {
        Navbar,
        Header,
       SMdialog,
    },
  data() {
    return {
      
    }
  },

  methods: {

  },
}
</script>
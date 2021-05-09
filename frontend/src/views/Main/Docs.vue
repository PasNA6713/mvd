<template>
  <v-container style='margin-top: 60px;'>
    <v-row :justify='isLoaded || !preview_loaded ? "center" : "space-between"'>
      <v-col cols="3">
        <v-row>
          <v-file-input
            chips
            multiple
            accept="application/pdf"
            append-icon="mdi-upload"
            prepend-icon=""
            label="Загрузите документы"
            outlined
            rounded
            solo
            ref="files"
            v-model="files"
          >
            <template v-slot:selection="data">
              <v-chip>
                {{ data.text }}
              </v-chip>
            </template>
            ></v-file-input
          >
        </v-row>

        <v-row justify="center">
          <v-btn text x-large dark @click="submitFiles">Загрузить</v-btn>
        </v-row>
      </v-col>

      <v-col v-if="preview_loaded" style="padding-top: 0; margin-left: 40px;">
        <v-row>
          <v-col
            cols="4"
            v-for="(file, index) in Object.keys(files_urls)"
            :key="index"
            style="padding-top: 0"
          >
            <v-card
              elevation="6"
              style="border: 2px solid rgba(0, 0, 0, 0.2); border-radius: 20px"
              class="mt-3"
            >
              <v-card-title>{{ file }}</v-card-title>
              <v-card-text>
                <iframe
                  width="100%"
                  height="400"
                  style="position: relative; z-index: 10"
                  :src="files_urls[file]"
                >
                </iframe>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-col>
    </v-row>

    <v-row justify='center'>
      <v-col cols="8" v-if="isLoaded">
        <v-card elevation="0" style="border-radius: 20px">
          <v-btn
            fab
            top
            right
            absolute
            elevation="0"
            @click="
              response = {};
              isLoaded = false;
            "
            style="border: 1px solid rgba(0, 0, 0, 0.2)"
          >
            <v-icon>mdi-close-thick</v-icon>
          </v-btn>
          <v-card
            v-for="(key, index) in Object.keys(response)"
            :key="index"
            elevation="6"
            style="border: 2px solid rgba(0, 0, 0, 0.2); border-radius: 20px; margin-top: 40px;"
          >
            <v-card-title>{{ key }} </v-card-title>
            <v-card-text>
              <v-row class="p-3">
                <v-col>
                  <iframe
                    width="100%"
                    height="400"
                    style="position: relative; z-index: 10"
                    :src="`${$store.state.backendUrl}/file/view/${response[key].id}/`"
                  >
                  </iframe>
                </v-col>

                <v-col>
                  <iframe
                    width="100%"
                    height="400"
                    style="position: relative; z-index: 10"
                    :src="`${$store.state.backendUrl}/file/view/formated/${response[key].id}/`"
                  >
                  </iframe>
                </v-col>
              </v-row>
            </v-card-text>
          </v-card>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>



<script>
export default {
  name: "Docs",
  components: {},

  data: () => ({
    files: null,
    files_urls: {},
    preview_loaded: false,
    preview: 0,

    response: {},
    loaded: 0,
    isLoaded: false,
  }),

  watch: {
    files(v) {
      console.log(v);
      if (v != null) {
        if (v[0]) {
          this.loaded = 0;
          this.isLoaded = null;
          this.response = {};
          v.forEach((e) => {
            var reader = new FileReader();
            reader.onload = (event) => {
              this.files_urls[e.name] = event.target.result;
              this.preview += 1;
            };
            reader.readAsDataURL(e);
          });
        } else {
          this.files_urls = {};
          this.preview_loaded = false;
          this.preview = 0;
        }
      } else {
        this.files_urls = {};
        this.preview_loaded = false;
        this.preview = 0;
      }
    },

    preview(data) {
      if (data != 0) {
        if (data == this.files.length) {
          this.preview = 0;
          this.preview_loaded = true;
        }
      }
    },

    loaded(data) {
      if (data != 0) {
        if (data == this.files.length) {
          this.loaded = 0;
          this.files = null;
          this.isLoaded = true;
        }
      }
    },
  },

  methods: {
    submitFiles() {
      this.response = [];
      this.isLoaded = false;
      this.files.forEach((file) => {
        let data = new FormData();
        data.append("file", file, file.name);
        axios({
          method: "POST",
          url: `${this.$store.state.backendUrl}/file/upload/`,
          data: data,
          headers: {
            Authorization: `Token ${this.$store.state.token}`,
            "Content-Type": "multipart/form-data",
            "Content-Disposition": `attachment; filename=${file.name}`,
          },
        }).then((r) => {
          this.response[file.name] = r.data;
          this.loaded += 1;
        });
      });
    },
  },
};
</script>


<style lang="scss">
</style>
<template>
    <v-card v-if="message" style='border: 1px solid rgba(0,0,0,0.2); border-radius: 20px;' elevation='0'>
          <v-card-title>{{ message.title }}</v-card-title>

          <v-card-text>
            <v-expansion-panels>
              <v-expansion-panel style='border: 1px solid rgba(0,0,0,0.1); border-radius: 20px;'>
                <v-expansion-panel-header>
                  <v-col>
                    <v-row justify="space-around">
                      <v-col>
                        <b
                          ><a
                            :href="message.link"
                            target="_blank"
                            rel="noreferrer"
                            >Источник</a
                          ></b
                        >
                      </v-col>

                      <v-col>
                        <b>{{
                          new Date(message.posted).toLocaleDateString("ru")
                        }}</b>
                      </v-col>
                    </v-row>

                    <v-row class="px-3 my-2">
                      <b>Организации: </b> {{ message.org.join(", ") }}
                    </v-row>
                    <v-row class="px-3 my-2">
                      <b>Люди: </b> {{ message.per.join(", ") }}
                    </v-row>
                    <v-row class="px-3 my-2">
                      <b>Места: </b> {{ message.loc.join(", ") }}
                    </v-row>
                  </v-col>
                </v-expansion-panel-header>

                <v-expansion-panel-content>
                  <v-row v-html="message.text" class="px-3"> </v-row>
                </v-expansion-panel-content>
              </v-expansion-panel>
            </v-expansion-panels>
          </v-card-text>
        </v-card>
</template>

<script>
export default {
  name: "FullMessage",

  props: {
    message: {
      required: true,
    },
  }
};
</script>


<style scoped>
.v-expansion-panel::before {
  box-shadow: 0;
}
</style>
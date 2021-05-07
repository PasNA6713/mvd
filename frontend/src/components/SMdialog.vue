
<template>
  <div class="px-8 my-10">
    <v-row>
      <div>
        <v-col class="mb-5 pa-0">
          <v-card width="500">
            <v-card-title class="white--text orange darken-4">
              Новые публикации
            </v-card-title>

            <DynamicScroller
              class="scroller"
              :items="items"
              :min-item-size="200"
              :style="'height: 700px'"
            >
              <template v-slot="{ item, index, active }">
                <DynamicScrollerItem
                  :item="item"
                  :active="active"
                  :size-dependencies="[item]"
                  :data-index="index"
                >
                  <div
                    :class="'pa-' + (item.isSelect ? 2 : 5)"
                    @click="
                      {
                        for (let i = 0; i < items.length; i++) {
                          items[i].isSelect = false;
                        }
                        item.isSelect = !item.isSelect;
                      }
                    "
                  >
                    <v-hover v-slot="{ hover }" close-delay="50">
                      <v-card
                        :color="hover || item.isSelect ? `#37889A` : `#385F73`"
                        dark
                        :class="{ 'on-hover': hover }"
                      >
                        <v-card-title class="text-h10">
                          Сообщение
                        </v-card-title>

                        <v-card-subtitle>{{ item.namef }}</v-card-subtitle>

                        <v-card-actions> </v-card-actions>
                      </v-card>
                    </v-hover>
                  </div>
                </DynamicScrollerItem>
              </template>
            </DynamicScroller>
          </v-card>
          <div>
            <v-card color="#385F73" dark class="mt-5"> фильтры </v-card>
          </div>
          <v-btn class="my-5" outlined color="#37889A" width="500" > Старт </v-btn>
        </v-col>
      </div>
      <v-btn v-on:click="adding"> Добавить </v-btn>
      <div  class="ml-10">
        <v-col class="mb-5 pa-0">
          
            <v-card color="#385F73" dark shaped>
              <v-card-title class="text-h10"> Сообщение </v-card-title>

              <v-card-subtitle>{{}}</v-card-subtitle>
            </v-card>
          
          <v-card color="#385F73" dark class="mt-5"> фильтры </v-card>
          <v-card width="1200" class="mt-5">
            
            <v-card-title class="white--text orange darken-4">
              Новые публикации
            </v-card-title>

            <DynamicScroller
              class="scroller"
              :items="items"
              :min-item-size="200"
              :style="'height: 600px'"
            >
              <template v-slot="{ item, index, active }">
                <DynamicScrollerItem
                  :item="item"
                  :active="active"
                  :size-dependencies="[item]"
                  :data-index="index"
                >
                    <div class="pa-5">
            <v-card color="#385F73" dark shaped>
              <v-card-title class="text-h10"> Сообщение </v-card-title>

              <v-card-subtitle>{{}}</v-card-subtitle>
            </v-card>
          </div>
                </DynamicScrollerItem>
              </template>
            </DynamicScroller>
          </v-card>
        </v-col>
      </div>
    </v-row>
  </div>
</template>









<style scoped>
.scroller {
  height: 100%;
}
</style>


<script>
import Vue from "vue";
import { DynamicScroller } from "vue-virtual-scroller";
Vue.component("DynamicScroller", DynamicScroller);
import "vue-virtual-scroller/dist/vue-virtual-scroller.css";

import { DynamicScrollerItem } from "vue-virtual-scroller";
Vue.component("DynamicScrollerItem", DynamicScrollerItem);
import "vue-virtual-scroller/dist/vue-virtual-scroller.css";

export default {
  name: "SMdialog",
  data: () => ({
    items: [],
  }),

  computed: {},

  methods: {
    adding() {
      this.items.unshift({
        namef: `kek`,
        id: this.items.length + 1,
        isSelect: false,
      });
    },
  },

  created() {
    this.connection = new WebSocket(
      `wss://mozh-team.net.ru/ws/${this.$store.state.token}/`
    );
    this.connection.onopen = function (event) {
      console.log(event);
      console.log("Робит");
    };
    this.connection.onmessage = function (event) {
      console.log(" " + event.data);
    };
  },

  mounted() {
    axios({
      method: "POST",
      url: `${this.$store.state.backendUrl}/chat/send/`,
      headers: {
        Authorization: `Token ${this.$store.state.token}`,
      },
    }).then((response) => {
      console.log("itsWork");
    });
  },
};
</script>

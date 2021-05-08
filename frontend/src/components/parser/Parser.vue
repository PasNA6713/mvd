
<template>
  <v-container>
    <v-row>
      <v-col cols="3">
        <v-row>
          <v-col>
            <v-card
              elevation="0"
              width="100%"
              style="border-radius: 20px; background: rgba(0, 0, 0, 0.1)"
              class="p-3"
            >
              <v-card-text>
                <v-row>
                  <v-col>
                    <v-select
                      :items="['meduza', 'instagram', 'pikabu']"
                      label="Выберите паука"
                      v-model="spider"
                      outlined
                      rounded
                      solo
                      dense
                    >
                    </v-select>
                  </v-col>
                </v-row>

                <v-row>
                  <v-col>
                    <v-row justify="center">
                      <v-btn text dark x-large @click="startCrawl()">
                        Старт
                      </v-btn>
                    </v-row>
                  </v-col>
                </v-row>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>

        <v-row>
          <v-card
            width="100%"
            elevation="0"
            style="background: rgba(0, 0, 0, 0)"
          >
            <DynamicScroller
              class="scroller"
              :items="items"
              :min-item-size="200"
              style='height: 900px;'
            >
              <template v-slot="{ item, index, active }">
                <DynamicScrollerItem
                  :item="item"
                  :active="active"
                  :size-dependencies="[item]"
                  :data-index="index"
                  class="px-3 py-4 md-5"
                >
                  <ShortMessage :message="item" @send-id="getId" />
                </DynamicScrollerItem>
              </template>
            </DynamicScroller>
          </v-card>
        </v-row>
      </v-col>

      <v-col>
        <v-row>
          <v-col>
            <v-card
              elevation="0"
              width="100%"
              style="border-radius: 20px; background: rgba(0, 0, 0, 0.1)"
              class="px-3"
            >
              <v-card-text>
                <v-row>
                  <v-col>
                    <v-autocomplete
                      v-model="locations"
                      :items="curMessage.loc"
                      dense
                      chips
                      label="Места"
                      small-chips
                      multiple
                      solo
                      rounded
                      clearable
                      style="background: rgba(0, 0, 0, 0)"
                    ></v-autocomplete>
                  </v-col>

                  <v-col>
                    <v-autocomplete
                      v-model="mans"
                      :items="curMessage.per"
                      dense
                      chips
                      label="Люди"
                      small-chips
                      multiple
                      rounded
                      solo
                      clearable
                    ></v-autocomplete>
                  </v-col>

                  <v-col>
                    <v-menu
                      v-model="menu"
                      :close-on-content-click="false"
                      :nudge-right="40"
                      transition="scale-transition"
                      offset-y
                      min-width="auto"
                    >
                      <template v-slot:activator="{ on, attrs }">
                        <v-text-field
                          v-model="date"
                          label="Даты"
                          append-icon="mdi-calendar"
                          readonly
                          v-bind="attrs"
                          v-on="on"
                          rounded
                          solo
                          dense
                        ></v-text-field>
                      </template>
                      <v-date-picker
                        v-model="date"
                        range
                        no-title
                      ></v-date-picker>
                    </v-menu>
                  </v-col>
                </v-row>

                <v-row>
                  <v-col>
                    <v-autocomplete
                      v-model="organizations"
                      :items="curMessage.org"
                      dense
                      chips
                      label="Организации"
                      small-chips
                      multiple
                      rounded
                      solo
                      clearable
                    ></v-autocomplete>
                  </v-col>

                  <v-col>
                    <v-select
                      :items="['meduza', 'instagram', 'pikabu']"
                      v-model="source"
                      solo
                      rounded
                      dense
                      label="Источник"
                    >
                    </v-select>
                  </v-col>

                  <v-col>
                    <v-row justify="center">
                      <v-btn text dark x-large @click="findNews">
                        Найти новости по тематике
                      </v-btn>
                    </v-row>
                  </v-col>
                </v-row>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>

        <FullMessage
          class="mt-3"
          v-if="!curMessage.test"
          :message="curMessage"
        />

        <v-card
          v-if="news"
          width="100%"
          elevation="0"
          style="background: rgba(0, 0, 0, 0)"
        >
          <v-card-title> Схожие сообщения </v-card-title>
          <v-card-text>
            <DynamicScroller
              class="scroller"
              :items="news"
              :min-item-size="200"
              :style="'height: 500px'"
            >
              <template v-slot="{ item, index, active }">
                <DynamicScrollerItem
                  :item="item"
                  :active="active"
                  :size-dependencies="[item]"
                  :data-index="index"
                  class="px-3 py-4 md-5"
                >
                  <FullMessage :message="item" @send-id="getId" />
                </DynamicScrollerItem>
              </template>
            </DynamicScroller>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>



<script>
import { DynamicScroller, DynamicScrollerItem } from "vue-virtual-scroller";
import "vue-virtual-scroller/dist/vue-virtual-scroller.css";

import ShortMessage from "./ShortMessage.vue";
import FullMessage from "./FullMessage.vue";

export default {
  name: "SMdialog",

  components: {
    DynamicScroller,
    DynamicScrollerItem,
    ShortMessage,
    FullMessage,
  },

  data: () => ({
    menu: false,

    items: [],
    news: null,
    spider: "meduza",
    curMessage: {
      loc: [],
      org: [],
      per: [],
      test: true,
    },

    locations: null,
    organizations: null,
    mans: null,
    source: null,
    date: null,
  }),

  methods: {
    add(val) {
      this.items.unshift(val);
    },

    getId(id) {
      axios
        .get(`${this.$store.state.backendUrl}/crawl/news/${id}/`)
        .then((r) => {
          console.log(r.data);
          this.curMessage = r.data;
        });
    },

    startCrawl() {
      axios({
        method: "POST",
        url: `${this.$store.state.backendUrl}/crawl/start/`,
        data: {
          spider_name: this.spider,
        },
      });
    },

    findNews() {
      let before = null;
      let after = null;
      if (this.date) {
        if (this.date[1]) before = new Date(this.date[1]).toISOString();
        if (this.date[0]) after = new Date(this.date[0]).toISOString();
      }
      axios({
        method: "GET",
        url: `${this.$store.state.backendUrl}/crawl/news/`,
        params: {
          loc: this.locations,
          per: this.mans,
          org: this.organizations,
          source: this.source,
          posted_after: after,
          posted_before: before,
        },
      }).then((r) => {
        this.news = r.data;
      });
    },
  },

  created() {
    this.connection = new WebSocket(
      `ws://127.0.0.1:8000/ws/${this.$store.state.token}/`
    );

    this.connection.onmessage = (event) => {
      let s = event.data.replace(/\\xa0/g, " ").replace(/'/g, '"');
      this.add(JSON.parse(s));
    };
  },
};
</script>


<style lang="scss" scoped>
.scroller {
  height: 100%;
}
</style>
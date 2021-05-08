<template>
    <v-card
      color="rgba(234, 234, 234, 1)"
      class="p-3"
      style="border-radius: 20px;"
      elevation='0'
    >
      <v-row style="display: contents;">
        <v-col>
          <v-row justify='space-around' class='mb-1 pl-3'>
            <v-col>
              <div>
                <b><a :href='message.source' target='_blank' rel='noreferrer'>Источник</a></b>
              </div>
            </v-col>
            <v-col>
              <div class="mt-1" style="color: rgba(0, 0, 0, 0.5)">
                {{ formatDate(message.posted) }}
              </div>
            </v-col>
          </v-row>

          <v-row class='mt-2' style="display: contents;">
            {{ message.text }}
          </v-row>
        </v-col>
      </v-row>

      <v-btn fab absolute bottom right small color='white'
      @click='sendId'>
          <v-icon>mdi-eye</v-icon>
      </v-btn>
    </v-card>
</template>

<script>
export default {
  name: "ShortMessage",

  props: {
    message: {
      required: true,
    },
  },

  data: () => ({
    months: [
      "января",
      "февраля",
      "марта",
      "апреля",
      "мая",
      "июня",
      "июля",
      "августа",
      "сентября",
      "октября",
      "ноября",
      "декабря",
    ],
  }),

  methods: {
    sendId() {
        this.$emit('send-id', this.message.id)
    },

    formatDate(date) {
      if (typeof date == "string") date = new Date(date);
      let minutes = date.getMinutes();
      if (minutes < 10) minutes = "0" + minutes;
      return (
        date.getDate() +
        " " +
        this.months[date.getMonth()] +
        " " +
        date.getHours() +
        ":" +
        minutes
      );
    }
  }
};
</script>


<style scoped>
</style>
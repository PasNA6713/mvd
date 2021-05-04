<script>
import { Bar, mixins } from "vue-chartjs"
const { reactiveProp } = mixins

export default {
  extends: Bar, 
  mixins: [reactiveProp],
  props: ['options'],

  data() {
    return {
      gradient: null,
    }
  },
  mounted() {
    this.renderChart(this.chartData, {
      responsive: true,
      maintainAspectRatio: false,
      
      onClick: function(event, pointsArray) {
        if(pointsArray.length === 1) {
          var pointPosition = pointsArray[0]._index
          var pointValue = this.tooltip._data.datasets[0].data[pointPosition]
          console.log(pointValue)
        } else {
            console.log("You selected the background!")            
        }  
      }
    })
  }
}
</script>
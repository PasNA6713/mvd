<template>
<div>
  <v-btn icon class="filter-icon"
  style="margin-left: 108px"
    @click.stop="drawer = !drawer">
    <v-icon>mdi-filter</v-icon>
  </v-btn>

  <v-card class="map-filter-container">
    <v-navigation-drawer
    fixed
    absolute
    temporary
    v-model="drawer"
    width="100%"
    height="40vh"
    >
      <v-list
        dense
        nav
        style="display: flex; align-items: baseline"
      >
        <v-list-item>
					<v-autocomplete class="map-filter__region"
					:items="filterData.city"
					v-model="chosedData.city"
					label="Город"
				></v-autocomplete>
        </v-list-item>

        <v-list-item>
          <v-autocomplete class="map-filter__region"
            :items="filterData.region"
            v-model="chosedData.region"
            label="Регион"
          ></v-autocomplete>
        </v-list-item>

        <v-list-item>
          <v-autocomplete class="map-filter__category"
            :items="filterData.category"
            v-model="chosedData.category"
            label="Категория"
          ></v-autocomplete>
        </v-list-item>

        <v-list-item>
          <v-autocomplete class="map-filter__light"
            :items="filterData.light"
            v-model="chosedData.light"
            label="Освещение"
					></v-autocomplete>
        </v-list-item>
            
        <v-list-item>
          <v-menu
            ref="menu"
            v-model="menu"
            :close-on-content-click="false"
            :return-value.sync="chosedData.date"
            transition="scale-transition"
            offset-y
            min-width="auto"
            >
            <template v-slot:activator="{ on, attrs }">
              <v-text-field
                v-model="chosedData.date"
                label="Даты"
                prepend-icon="mdi-calendar"
                readonly
                v-bind="attrs"
                v-on="on"
              ></v-text-field>
            </template>
            <v-date-picker
              v-model="chosedData.date"
              :color="theme.color"
              width="600px"
              range
              locale="ru"
              no-title
              scrollable
              :show-current="false"
            >
              <v-spacer></v-spacer>
              <v-btn
                text
                color="primary"
                @click="menu = false"
              >
                Cancel
              </v-btn>
              <v-btn
                text
                color="primary"
                @click="$refs.menu.save(chosedData.date)"
              >
                OK
              </v-btn>
            </v-date-picker>
          </v-menu>
        </v-list-item>    
        
        <v-list-item>
          <v-select class="map-filter__time"
          v-model="chosedData.timeGroup"
          :items="Object.keys(filterData.timeGroup[0])"
          label="Время"
          >
          </v-select>
        </v-list-item>
			</v-list>

			<v-list
        dense
        nav
        style="display: flex; align-items: baseline"
      >
				<v-list-item>
					<v-autocomplete class="map-filter__light"
            :items="filterData.address"
            v-model="chosedData.address"
            label="Адрес"
					></v-autocomplete>
				</v-list-item>

				<v-list-item>
					<v-autocomplete class="map-filter__light"
            :items="filterData.organization"
            v-model="chosedData.organization"
            label="Организация"
					></v-autocomplete>
				</v-list-item>

				<v-list-item>
					<v-autocomplete class="map-filter__light"
            :items="filterData.criminalType"
            v-model="chosedData.criminalType"
            label="Тип преследования"
					></v-autocomplete>
				</v-list-item>

				<v-list-item>
					<v-autocomplete class="map-filter__light"
            :items="filterData.employee"
            v-model="chosedData.employee"
            label="Работник"
					></v-autocomplete>
				</v-list-item>

				<v-list-item>
					<v-autocomplete class="map-filter__light"
            :items="filterData.isOperative"
            v-model="chosedData.isOperative"
            label="В процессе"
					></v-autocomplete>
				</v-list-item>

				<v-list-item>
					<v-autocomplete class="map-filter__light"
            :items="filterData.crimeQualification"
            v-model="chosedData.crimeQualification"
            label="Квалификация преступления"
					></v-autocomplete>
				</v-list-item>
			</v-list>

			<v-list
        dense
        nav
        style="display: flex; align-items: baseline"
      >
				<v-list-item>
					<v-autocomplete class="map-filter__light"
            :items="filterData.ykQualification"
            v-model="chosedData.ykQualification"
            label="УК квалификация"
					></v-autocomplete>
				</v-list-item>

				<v-list-item>
					<v-autocomplete class="map-filter__light"
            :items="filterData.severity"
            v-model="chosedData.severity"
            label="Строгость"
					></v-autocomplete>
				</v-list-item>

				<v-list-item>
					<v-autocomplete class="map-filter__light"
            :items="filterData.isAttempt"
            v-model="chosedData.isAttempt"
            label="Это попытка"
					></v-autocomplete>
				</v-list-item>

				<v-list-item>
					<v-autocomplete class="map-filter__light"
            :items="filterData.damage"
            v-model="chosedData.damage"
            label="Ущерб"
					></v-autocomplete>
				</v-list-item>

				<v-list-item>
					<v-autocomplete class="map-filter__light"
            :items="filterData.crimeDirection"
            v-model="chosedData.crimeDirection"
            label="Направление преступления"
					></v-autocomplete>
				</v-list-item>

				<v-list-item>
					<v-autocomplete class="map-filter__light"
            :items="filterData.money"
            v-model="chosedData.money"
            label="Деньги"
					></v-autocomplete>
				</v-list-item>
      </v-list>

			<v-list
        dense
        nav
        style="display: flex; align-items: baseline"
      >
			<v-list-item>
					<v-autocomplete class="map-filter__light"
            :items="filterData.drugName"
            v-model="chosedData.drugName"
            label="Наркотики"
					></v-autocomplete>
				</v-list-item>

				<v-list-item>
					<v-autocomplete class="map-filter__light"
            :items="filterData.drugWeight"
            v-model="chosedData.drugWeight"
            label="Вес наркотиков"
					></v-autocomplete>
				</v-list-item>

				<v-list-item>
					<v-autocomplete class="map-filter__light"
            :items="filterData.victimNumber"
            v-model="chosedData.victimNumber"
            label="Количество пострадавших"
					></v-autocomplete>
				</v-list-item>

				<v-list-item>
					<v-autocomplete class="map-filter__light"
            :items="filterData.deadNum"
            v-model="chosedData.deadNum"
            label="Количество погибших"
					></v-autocomplete>
				</v-list-item>

        <v-list-item>
          <div class="filter-buttons">
            <v-btn color="#EDAC48" @click="clearForm"><v-icon>mdi-backspace-reverse</v-icon></v-btn>
            <v-btn class="filter-buttons__button" color="#EDAC48" @click="getData"><v-icon>mdi-find-replace</v-icon>Показать на таблице</v-btn>
          </div>
        </v-list-item>
			</v-list>

    </v-navigation-drawer>
  </v-card>
</div>
</template>

<style lang="scss" scoped>
@import '@/styles/common.scss';
@import '@/styles/views/stat.scss';
</style>

<script>
export default {
  name: "StatFilter",
  props: {
    theme: Object
  },
  data() {
    return {
      filterData: {
        region: [],
        light: [],
        category: [],
        timeGroup: [
          {
            "Все время": 0,
            "2.00 - 11.00": 1, 
            "11.00 - 16.00": 2, 
            "16.00 - 21.00": 3, 
            "21.00 - 2.00": 4
          }
        ],
        city: [],
				address: [],
				organization: [],
				criminalType: [],
				employee: [],
				isOperative: [],
				crimeQualification: [],
				ykQualification: [],
				severity: [],
				isAttempt: [],
				damage: [],
				crimeDirection: [],
				money: [],
				drugName: [],
				drugWeight: [],
				victimNumber: [],
				deadNum: []
      },

      chosedData: {
        date: ["", new Date().toISOString().substr(0, 10)],
        timeGroup: "Все время",
        region: "",
        light: "",
        category: "",
        city: "",
				address: "",
				organization: "",
				criminalType: "",
				employee: "",
				isOperative: "",
				crimeQualification: "",
				ykQualification: "",
				severity: "",
				isAttempt: "",
				damage: "",
				crimeDirection: "",
				money: "",
				drugName: "",
				drugWeight: "",
				victimNumber: "",
				deadNum: ""
      },

      menu: false,
      drawer: false,
    }
  },

  computed: {
    filterParams() {
      let filterData = {
        region: this.chosedData.region,
        light: this.chosedData.light,
        category: this.chosedData.category,
        datetime_before: (this.chosedData.date[1]) ? `${this.chosedData.date[1]}T00:00:00Z` : "", 
        datetime_after: (this.chosedData.date[0]) ? `${this.chosedData.date[0]}T00:00:00Z` : "",
        time_group: this.filterData.timeGroup[0][this.chosedData.timeGroup],
        city: this.chosedData.city,
				address: this.chosedData.address,
				organization: this.chosedData.organization,
				criminal_type: this.chosedData.criminalType,
				employee: this.chosedData.employee,
				is_operative: this.chosedData.isOperative,
				crime_qualification: this.chosedData.crimeQualification,
				yk_qualification: this.chosedData.ykQualification,
				severity: this.chosedData.severity,
				is_attempt: this.chosedData.isAttempt,
				damage: this.chosedData.damage,
				crime_direction: this.chosedData.crimeDirection,
				money: this.chosedData.money,
				drug_name: this.chosedData.drugName,
				drug_weight: this.chosedData.drugWeight,
				victim_number: this.chosedData.victimNumber,
				dead_num: this.chosedData.deadNum,
      }
      return filterData
    }
  },

  methods: {
    async getFilterData() {
      await axios.get(`${this.$store.state.backendUrl}/map/get-filter-params/region/`
      ).then(response => { this.filterData.region = response.data })

      await axios.get(`${this.$store.state.backendUrl}/map/get-filter-params/category/`
      ).then(response => { this.filterData.category = response.data })

      await axios.get(`${this.$store.state.backendUrl}/map/get-filter-params/light/`
      ).then(response => { this.filterData.light = response.data })

      await axios.get(`${this.$store.state.backendUrl}/map/get-filter-params/parent_region/`
      ).then(response => { this.filterData.city = response.data })

      await axios.get(`${this.$store.state.backendUrl}/map/get-filter-params/address/`
      ).then(response => { this.filterData.address = response.data })
			
      await axios.get(`${this.$store.state.backendUrl}/map/get-filter-params/organization/`
      ).then(response => { this.filterData.organization = response.data })
			
      await axios.get(`${this.$store.state.backendUrl}/map/get-filter-params/criminal_type/`
      ).then(response => { this.filterData.criminalType = response.data })
			
      await axios.get(`${this.$store.state.backendUrl}/map/get-filter-params/employee/`
      ).then(response => { this.filterData.employee = response.data })
			
      await axios.get(`${this.$store.state.backendUrl}/map/get-filter-params/is_operative/`
      ).then(response => { this.filterData.isOperative = response.data })
			
      await axios.get(`${this.$store.state.backendUrl}/map/get-filter-params/crime_qualification/`
      ).then(response => { this.filterData.crimeQualification = response.data })
			
      await axios.get(`${this.$store.state.backendUrl}/map/get-filter-params/yk_qualification/`
      ).then(response => { this.filterData.ykQualification = response.data })
			
      await axios.get(`${this.$store.state.backendUrl}/map/get-filter-params/severity/`
      ).then(response => { this.filterData.severity = response.data })
			
      await axios.get(`${this.$store.state.backendUrl}/map/get-filter-params/is_attempt/`
      ).then(response => { this.filterData.isAttempt = response.data })
			
      await axios.get(`${this.$store.state.backendUrl}/map/get-filter-params/damage/`
      ).then(response => { this.filterData.damage = response.data })
			
      await axios.get(`${this.$store.state.backendUrl}/map/get-filter-params/crime_direction/`
      ).then(response => { this.filterData.crimeDirection = response.data })
			
      await axios.get(`${this.$store.state.backendUrl}/map/get-filter-params/money/`
      ).then(response => { this.filterData.money = response.data })
			
      await axios.get(`${this.$store.state.backendUrl}/map/get-filter-params/drug_name/`
      ).then(response => { this.filterData.drugName = response.data })
			
      await axios.get(`${this.$store.state.backendUrl}/map/get-filter-params/drug_weight/`
      ).then(response => { this.filterData.drugWeight = response.data })
			
      await axios.get(`${this.$store.state.backendUrl}/map/get-filter-params/victim_number/`
      ).then(response => { this.filterData.victimNumber = response.data })
			
      await axios.get(`${this.$store.state.backendUrl}/map/get-filter-params/dead_num/`
      ).then(response => { this.filterData.deadNum = response.data })
			
    },

    getData() {
			this.drawer = false
      this.$emit("get-data", this.filterParams)
    },

    clearForm() {
        this.chosedData.region = ""
        this.chosedData.light = ""
        this.chosedData.category = ""
        this.chosedData.timeGroup = "Все время"
        this.chosedData.date = ["", new Date().toISOString().substr(0, 10)] 
        this.chosedData.city = ""
				this.chosedData.address = ""
				this.chosedData.organization = ""
				this.chosedData.criminalType = ""
				this.chosedData.employee = ""
				this.chosedData.isOperative = ""
				this.chosedData.crimeQualification = ""
				this.chosedData.ykQualification = ""
				this.chosedData.severity = ""
				this.chosedData.isAttempt = ""
				this.chosedData.damage = ""
				this.chosedData.crimeDirection = ""
				this.chosedData.money = ""
				this.chosedData.drugName = ""
				this.chosedData.drugWeight = ""
				this.chosedData.victimNumber = ""
				this.chosedData.deadNum = ""
    },
  },

  created() {
    this.getFilterData()
  }
}
</script>
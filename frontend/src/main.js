import './index.css'

import { createApp } from 'vue'
import router from './router'
import App from './App.vue'

import { Button, setConfig, frappeRequest, resourcesPlugin } from 'frappe-ui'

// ✅ ADD THIS
import VueApexCharts from "vue3-apexcharts"

let app = createApp(App)

setConfig('resourceFetcher', frappeRequest)

app.use(router)
app.use(resourcesPlugin)

// ✅ REGISTER CHART PLUGIN
app.use(VueApexCharts)

app.component('Button', Button)

app.mount('#app')
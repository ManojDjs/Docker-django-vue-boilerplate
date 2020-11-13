import { createApp ,h} from 'vue'
import App from './App.vue'

import WaveUI from 'wave-ui'
import 'wave-ui/dist/wave-ui.css'
import router from '@/router/index.js' // <---



const app = createApp({
  render: () => h(App)
})

new WaveUI(app, {
  // Some Wave UI options.
})

app.use(router).mount('#app')
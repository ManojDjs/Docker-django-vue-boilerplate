import { createApp ,h} from 'vue'
import App from './App.vue'

import WaveUI from 'wave-ui'
import 'wave-ui/dist/wave-ui.css'
import router from '@/router/index.js' // <---
import store from './store';

import Button from 'primevue/button';
// import Dialog from 'primevue/dialog';
// import Sidebar from 'primevue/sidebar';

import Panel from 'primevue/panel';

import 'primevue/resources/themes/saga-blue/theme.css';
import 'primevue/resources/primevue.min.css';
import 'primeflex/primeflex.css';
import 'primeicons/primeicons.css';
import SelectButton from 'primevue/selectbutton';
import Menubar from 'primevue/menubar';
import TabMenu from 'primevue/tabmenu';
import BlockUI from 'primevue/blockui';
import InputText from 'primevue/inputtext';
import Card from 'primevue/card';
import Password from 'primevue/password';
import Fieldset from 'primevue/fieldset';
import ToastService from 'primevue/toastservice';
import Toast from 'primevue/toast';
import TabView from 'primevue/tabview';
import TabPanel from 'primevue/tabpanel';
import Dropdown from 'primevue/dropdown';
import RadioButton from 'primevue/radiobutton';
import Toolbar from 'primevue/toolbar';
import Chart from 'primevue/chart';
import Sidebar from 'primevue/sidebar';
import Ripple from 'primevue/ripple';
import ScrollPanel from 'primevue/scrollpanel';
import Timeline from 'primevue/timeline';
import Slider from 'primevue/slider';
import InputNumber from 'primevue/inputnumber';

const app = createApp({
  render: () => h(App)
}).use(store).use(ToastService);

new WaveUI(app, {
  // Some Wave UI options.
})
app.component('InputNumber',InputNumber)
app.component('SelectButton',SelectButton)
app.component('Slider',Slider)
app.component('Timeline',Timeline)
app.component('ScrollPanel',ScrollPanel)
app.component('Sidebar',Sidebar)
app.component('Panel',Panel)
app.component('Chart',Chart)
app.component('RadioButton',RadioButton)
app.component('Toolbar',Toolbar)
app.component('Dropdown',Dropdown)
app.component('TabView',TabView)
app.component('TabPanel',TabPanel)
app.component('Toast',Toast)
app.component('Fieldset',Fieldset)
app.component('Password',Password)
app.component('Card',Card)
app.component('InputText',InputText)
app.component('BlockUI',BlockUI)
app.component('TabMenu',TabMenu)
app.component('Sidebar',Sidebar)
app.component('Button',Button)
app.component('Menubar',Menubar)
app.directive('ripple', Ripple);
app.use(router).mount('#app')

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import 'materialize-css'
import 'materialize-css/dist/css/materialize.min.css'
import M from 'materialize-css';
/*import 'material-design-icons/iconfont/material-icons.css'*/

document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.carousel');
    var instances = M.Carousel.init(elems, {
           duration: 150,
            dist: -80,
            shift: 5,
            padding: 5,
            numVisible: 3,
            indicators: true,
            noWrap: true
    });
}),

createApp(App).use(router).mount('#app')

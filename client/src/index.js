// Third party libs
import Vue from 'vue';
import VueResource from 'vue-resource';
import VueRouter from 'vue-router';
import Keen from 'keen-ui';

// Third party CSS
import 'bootstrap/dist/css/bootstrap.min.css';
import 'keen-ui/dist/min/keen-ui.min.css';

// Our libs
import ItemList from './item-list.vue';

// Our CSS
import './common.css';

// Load Vue plugins
Vue.use(VueResource);
Vue.use(VueRouter);
Vue.use(Keen);

// Initialize app and router
let App = Vue.extend({});
let router = new VueRouter({history: true});

// Scroll to the top of the page when we change pages
router.beforeEach(function(transition) {
    window.scrollTo(0, 0);
    transition.next();
});

// Track client-routed page views with Google Analytics
router.afterEach(function(transition) {
    ga('send', {hitType: 'pageview', page: transition.to.path});
});

// Routes
router.map({
    '/': {
        name: 'item_list',
        component: ItemList,
    },
});

// Bind app to the document body
router.start(App, 'body');

<style>
.page-header {
    border-bottom: none;
}
.snackbar-container {
    bottom: 0;
    left: 0;
    position: fixed;
    width: 100%;
}
.ui-snackbar {
    max-width: inherit;
}
</style>

<template>
    <ui-preloader :show="$loadingRouteData"></ui-preloader>
    <template v-if="!$loadingRouteData">
        <div class="container">
            <div class="page-header">
                <h1 class="text-center">hey you take this free stuff</h1>
            </div>

            <template v-for="item in items">
                <div class="row">
                    <div class="col-sm-12 col-md-8 col-md-offset-2">
                        <item :item="item" :has_been_claimed_init="claimed_items[item.id]"></item>
                    </div>
                </div>
            </template>

            <div class="page-header">
                <h1 class="text-center">seriously take it</h1>
            </div>
        </div>
    </template>
    <dibs-modal></dibs-modal>
    <div class="snackbar-container">
        <ui-snackbar-container></ui-snackbar-container>
    </div>
</template>

<script>
import DibsModal from './dibs-modal.vue';
import Item from './item.vue';

export default {
    components: {
        DibsModal,
        Item,
    },
    data() {
        return {
            items: [],
            claimed_items: {},
        };
    },
    events: {
        'dibs-modal.show': function(item) {
            let data = {
                item: item,
                has_been_claimed: this.claimed_items[item.id],
            };

            this.$broadcast('dibs-modal.show', data);
        },
        'claim-item': function(data) {
            let item = data.item;
            let username = data.username;
            let comments = data.comments;

            this.claimed_items[item.id] = true;
            this.$broadcast('claim-item', item);

            let post_data = {
                item_id: item.id,
                item_name: item.name,
                username: username,
                comments: comments,
            };

            this.$http.post('/claim-item', post_data, {emulateJSON: true}).then(function success(response) {
                this.$broadcast('ui-snackbar::create', {
                    message: "Request sent! If you don't hear back in a few days, it's because I'm ignoring you. <3",
                });
            }, function error(response) {
                this.$broadcast('ui-snackbar::create', {
                    message: "Whoops, some wires got crossed. Try that again or message me directly.",
                });
            });
        },
    },
    route: {
        data: function() {
            return this.$http.get('/items.json').then(function success(response) {
                let items = [];

                _.forEach(response.data.items, (item, item_id) => {
                    item.id = item_id;
                    items.push(item);
                });

                this.items = items;
                this.claimed_items = response.data.claimed_items;
            }, function error(response) {
            });
        },
    },
};
</script>

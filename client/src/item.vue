<style>
.item-panel {
    background-color: #fff;
    border-radius: 2px;
    box-shadow: 0 2px 8px rgba(0,0,0,.33);
    margin-bottom: 50px;
}
.item-panel-heading {
    padding: 24px 24px 8px;
}
.item-panel-title {
    margin: 0;
}
.item-panel-body {
    font-size: 16px;
    padding: 16px 24px 24px;
}
.item-panel-footer {
    margin-top: -8px;
    padding: 8px 24px 24px;
}
.ui-icon {
    cursor: default;
}
</style>

<template>
    <div class="item-panel">
        <div class="item-panel-heading">
            <h3 class="item-panel-title h2">{{ item.name }}</h3>
        </div>
        <div class="item-panel-body">

            <div class="row">
                <div class="col-xs-12 col-sm-4">
                    <a :href="item.bgg_link" class="thumbnail">
                        <img :src="item.thumbnail">
                    </a>
                </div>

                <div class="col-xs-12 col-sm-8">
                    <div class="item-description well">
                        {{ item.description }}
                    </div>

                    <div class="item-metadata">
                        <div>
                            <span v-el:player_count>
                                <ui-icon icon="people"></ui-icon>
                                {{ item.player_count }}
                            </span>
                        </div>

                        <div>
                            <span v-el:game_length>
                                <ui-icon icon="access_time"></ui-icon>
                                {{ item.game_length }}
                            </span>
                        </div>

                        <div>
                            <span v-el:complexity>
                                <ui-icon icon="lightbulb_outline"></ui-icon>
                                {{ item.complexity }}
                            </span>
                        </div>

                        <!-- Have to wait until after compilation to bind tooltips -->
                        <template v-if="is_compiled">
                            <ui-tooltip :trigger="$els.player_count" content="Players" position="right middle"></ui-tooltip>
                            <ui-tooltip :trigger="$els.game_length" content="Length" position="right middle"></ui-tooltip>
                            <ui-tooltip :trigger="$els.complexity" content="Complexity" position="right middle"></ui-tooltip>
                        </template>
                    </div>
                </div>
            </div>

        </div>
        <div class="item-panel-footer text-right">
            <template v-if="has_been_claimed">
                <ui-button color="danger" icon="do_not_disturb" @click="show_dibs_modal">NO BACKSIES</ui-button>
            </template>
            <template v-else>
                <ui-button color="primary" icon="add_circle" @click="show_dibs_modal">{{ button_text }}</ui-button>
            </template>
        </div>
    </div>
</template>

<script>
import _ from 'lodash';

const BUTTON_TEXTS = [
    'dibs',
    'gimme',
    'want',
    'yes plz',
];

export default {
    props: [
        'item',
    ],
    data() {
        return {
            button_text: _.sample(BUTTON_TEXTS),
            is_compiled: false,
            has_been_claimed: false,
        };
    },
    methods: {
        show_dibs_modal: function() {
            this.$dispatch('dibs-modal.show', this.item);
        },
    },
    compiled() {
        this.is_compiled = true;
    },
    events: {
        'claim-item': function(item) {
            if (item.id === this.item.id) {
                this.has_been_claimed = true;
            }
        },
    },
};
</script>

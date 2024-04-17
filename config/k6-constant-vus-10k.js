import http from 'k6/http';
import {sleep} from 'k6';

export default function () {
    http.get(__ENV.SERVICE_URL);
    sleep(2 * Math.random() + 1); // between 1s and 3s
}
export const options = {
    discardResponseBodies: true,
    scenarios: {
        contacts: {
            executor: 'constant-vus',
            vus: 10000,
            duration: '6m',
            gracefulStop: '3s',
        },
    },
};
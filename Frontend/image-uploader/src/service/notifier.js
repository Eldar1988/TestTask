import { Notify } from 'quasar'

export default function notifier(notify, color='dark') {
  Notify.create({message: `${notify}`, position: 'top', color: color})
}

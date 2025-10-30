
import { get, post } from './axios'

export const apiAddress = p => post('api-pm/reportKanban/yieldAchievementRate', p);
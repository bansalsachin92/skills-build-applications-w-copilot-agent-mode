from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from octofit_tracker.test_data import test_users, test_teams, test_activities, test_leaderboard, test_workouts

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Populate users
        for user_data in test_users:
            User.objects.get_or_create(
                username=user_data['username'],
                email=user_data['email'],
                defaults={'password': user_data['password']}
            )

        # Populate teams
        for team_data in test_teams:
            team, _ = Team.objects.get_or_create(name=team_data['name'])
            for member_username in team_data['members']:
                user = User.objects.get(username=member_username)
                team.members.add(user)

        # Populate activities
        for activity_data in test_activities:
            user = User.objects.get(username=activity_data['user'])
            Activity.objects.get_or_create(
                user=user,
                activity_type=activity_data['activity_type'],
                duration=activity_data['duration']
            )

        # Populate leaderboard
        for leaderboard_data in test_leaderboard:
            user = User.objects.get(username=leaderboard_data['user'])
            Leaderboard.objects.get_or_create(
                user=user,
                defaults={'score': leaderboard_data['score']}
            )

        # Populate workouts
        for workout_data in test_workouts:
            Workout.objects.get_or_create(
                name=workout_data['name'],
                defaults={'description': workout_data['description']}
            )

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))

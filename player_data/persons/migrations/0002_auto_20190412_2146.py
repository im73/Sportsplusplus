# Generated by Django 2.1.7 on 2019-04-12 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('日期', models.CharField(max_length=20)),
                ('主场球队中文名', models.CharField(max_length=20)),
                ('客场球队中文名', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Match_player',
            fields=[
                ('类型', models.IntegerField()),
                ('主客场', models.IntegerField()),
                ('球员名', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('位置', models.CharField(max_length=10)),
                ('时间', models.CharField(max_length=10)),
                ('投篮', models.CharField(max_length=10)),
                ('三分', models.CharField(max_length=10)),
                ('罚球', models.CharField(max_length=10)),
                ('前场', models.CharField(max_length=10)),
                ('后场', models.CharField(max_length=10)),
                ('篮板', models.CharField(max_length=10)),
                ('助攻', models.CharField(max_length=10)),
                ('犯规', models.CharField(max_length=10)),
                ('抢断', models.CharField(max_length=10)),
                ('失误', models.CharField(max_length=10)),
                ('封盖', models.CharField(max_length=10)),
                ('得分', models.CharField(max_length=10)),
                ('正负', models.CharField(max_length=10)),
                ('比赛id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='persons.Match')),
            ],
        ),
        migrations.CreateModel(
            name='Match_teamsummary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('主客场', models.IntegerField()),
                ('投篮', models.CharField(max_length=10)),
                ('三分', models.CharField(max_length=10)),
                ('罚球', models.CharField(max_length=10)),
                ('前场', models.CharField(max_length=10)),
                ('后场', models.CharField(max_length=10)),
                ('篮板', models.CharField(max_length=10)),
                ('助攻', models.CharField(max_length=10)),
                ('犯规', models.CharField(max_length=10)),
                ('抢断', models.CharField(max_length=10)),
                ('失误', models.CharField(max_length=10)),
                ('封盖', models.CharField(max_length=10)),
                ('得分', models.CharField(max_length=10)),
                ('投篮命中率', models.CharField(max_length=10)),
                ('三分命中率', models.CharField(max_length=10)),
                ('罚球命中率', models.CharField(max_length=10)),
                ('比赛id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='persons.Match')),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('第一节', models.IntegerField()),
                ('第二节', models.IntegerField()),
                ('第三节', models.IntegerField()),
                ('第四节', models.IntegerField()),
                ('总分', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='player',
            old_name='国际',
            new_name='国籍',
        ),
        migrations.AddField(
            model_name='career',
            name='类型',
            field=models.IntegerField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='选秀',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='球队中文名',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='career',
            name='三分',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='career',
            name='助攻',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='career',
            name='命中率',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='career',
            name='场次',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='career',
            name='失误',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='career',
            name='序号',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='persons.Player'),
        ),
        migrations.AlterField(
            model_name='career',
            name='得分',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='career',
            name='投篮',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='career',
            name='抢断',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='career',
            name='时间',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='career',
            name='犯规',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='career',
            name='盖帽',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='career',
            name='篮板',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='career',
            name='罚球',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='player',
            name='球队名',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='persons.Team'),
        ),
        migrations.AlterField(
            model_name='player',
            name='英文名',
            field=models.CharField(max_length=50),
        ),
    ]

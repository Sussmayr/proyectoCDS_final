{% extends "base.html" %}
{% block title %} Login Page {% endblock %}
{% block content %}
    {% with messages = get_flashed_messages() %}
        {% if messages %}
            {% for msg in messages %}
                <p>{{msg}}</p>
            {% endfor %}
        {% endif %}
    {% endwith %}

    <h3 class="form-signin-heading">Consultar {{user}}</h3>

    <table>
        <tr>
            <td>id</td>
            <td>Nombre</td>
            <td>Contrasena</td>
        </tr>
        <?php if(!$res) {?>
        <tr>
             <td colspan="6">No hay datos para mostrar</td>
        </tr>
        <?php }
        else {
        while($row=sqlsrv_connect($res)) {?>
        <tr>
             <td><?php echo $row['id'];?></td>
             <td><?php echo $row['Name'];?></td>
             <td><?php echo $row['pass'];?></td>
        </tr>
        <?php
        }//Fin while
        }//Fin if
        sqlsrv_close($con); ?>
    </table>


{% endblock %}
